import {canonical, validateItem, QuizQuestion, AppMode, OptionIndex} from '../types/quiz';
import {schema} from './schema';
export interface Database {
 execSync(sql:string):void;
 runSync(sql:string, params?: (string|number|null)[]):unknown;
 getFirstSync<T>(sql:string,params?: (string|number|null)[]):T|null;
 getAllSync<T>(sql:string,params?: (string|number|null)[]):T[];
 withTransactionSync(task:()=>void):void;
}
export function createRepository(db:Database) {
 return {
  init() {
   db.execSync('PRAGMA foreign_keys=ON; PRAGMA journal_mode=WAL;');
   const version=db.getFirstSync<{user_version:number}>('PRAGMA user_version')!.user_version;
   if(version>1) throw new Error('Banco criado por uma versão mais recente do aplicativo.');
   if(version===0) db.withTransactionSync(()=>db.execSync(schema));
  },
  importBatch(input:unknown) {
   if(!Array.isArray(input) || !input.every(validateItem)) throw new Error('Pacote de questões inválido.');
   const seen=new Set<string>();
   for(const item of input){if(seen.has(item.question.id)) throw new Error('ID duplicado no pacote.'); seen.add(item.question.id);}
   db.withTransactionSync(()=>{
    for(const item of input){
     const q=item.question; const payload=canonical(item);
     const old=db.getFirstSync<{payload:string}>('SELECT payload FROM questions WHERE id=? AND version=?',[q.id,q.version]);
     if(old){if(old.payload!==payload) throw new Error('Conteúdo alterado sem incrementar a versão.'); continue;}
     const latest=db.getFirstSync<{version:number,mode:string}>('SELECT version,mode FROM questions WHERE id=? ORDER BY version DESC LIMIT 1',[q.id]);
     if(latest && (latest.version>q.version || latest.mode!==item.mode)) throw new Error('Versão anterior ou módulo incompatível.');
     const category=item.mode==='oab'?item.question.discipline:item.question.category;
     db.runSync('INSERT INTO questions VALUES (?,?,?,?,?,?)',[q.id,q.version,item.mode,category,q.correctAnswer,payload]);
     q.options.forEach((o,i)=>db.runSync('INSERT INTO question_options VALUES (?,?,?,?)',[q.id,q.version,i,o]));
     if(item.mode==='oab') item.question.legalReferences.forEach((r,i)=>db.runSync('INSERT INTO question_references VALUES (?,?,?,?)',[q.id,q.version,i,r]));
    }
   });
  },
  list(mode:AppMode, category?:string):QuizQuestion[] {
   const rows=db.getAllSync<{payload:string}>(`SELECT q.payload FROM questions q WHERE q.mode=? AND (? IS NULL OR q.category=?) AND q.version=(SELECT MAX(v.version) FROM questions v WHERE v.id=q.id) ORDER BY q.id`,[mode,category??null,category??null]);
   return rows.map(r=>JSON.parse(r.payload) as QuizQuestion);
  },
  createSession(id:string, items:QuizQuestion[]) {
   if(!items.length) throw new Error('Partida vazia.');
   db.withTransactionSync(()=>{
    db.runSync('INSERT INTO sessions(id) VALUES (?)',[id]);
    items.forEach((item,i)=>db.runSync('INSERT INTO session_questions VALUES (?,?,?,?)',[id,i,item.question.id,item.question.version]));
   });
  },
  answer(session:string,id:string,version:number,option:OptionIndex):boolean {
   if(![0,1,2,3].includes(option)) throw new Error('Alternativa inválida.');
   let correct=false;
   db.withTransactionSync(()=>{
    const row=db.getFirstSync<{correct_answer:number,finished:number}>(`SELECT q.correct_answer,s.finished FROM session_questions sq JOIN questions q ON q.id=sq.question_id AND q.version=sq.question_version JOIN sessions s ON s.id=sq.session_id WHERE sq.session_id=? AND sq.question_id=? AND sq.question_version=?`,[session,id,version]);
    if(!row || row.finished) throw new Error('Questão não pertence a uma partida ativa.');
    const old=db.getFirstSync<{selected_option:number,is_correct:number}>('SELECT selected_option,is_correct FROM answers WHERE session_id=? AND question_id=?',[session,id]);
    if(old){if(old.selected_option!==option) throw new Error('Resposta já registrada.'); correct=!!old.is_correct; return;}
    correct=row.correct_answer===option;
    db.runSync('INSERT INTO answers(session_id,question_id,question_version,selected_option,is_correct) VALUES (?,?,?,?,?)',[session,id,version,option,correct?1:0]);
   });return correct;
  },
  finish(session:string) {
   let result={score:0,total:0};
   db.withTransactionSync(()=>{
    const total=db.getFirstSync<{n:number}>('SELECT COUNT(*) n FROM session_questions WHERE session_id=?',[session])!.n;
    const row=db.getFirstSync<{n:number,score:number}>('SELECT COUNT(*) n,COALESCE(SUM(is_correct),0) score FROM answers WHERE session_id=?',[session])!;
    if(!total || row.n!==total) throw new Error('Responda todas as questões.');
    db.runSync('UPDATE sessions SET finished=1 WHERE id=?',[session]);result={score:row.score,total};
   });return result;
  },
  stats(){return db.getFirstSync<{total:number,correct:number}>('SELECT COUNT(*) total,COALESCE(SUM(is_correct),0) correct FROM answers')!;}
 };
}
