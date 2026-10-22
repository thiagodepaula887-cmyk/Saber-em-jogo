(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.QuizEngine=api;})(typeof globalThis!=='undefined'?globalThis:this,function(){
 'use strict';
 const ladder=[100,200,300,500,1000,2000,3000,5000,10000,20000];
 function dayKey(d=new Date()){return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;}
 function hash(s){let n=2166136261;for(const c of s){n^=c.charCodeAt(0);n=Math.imul(n,16777619);}return n>>>0;}
 function daily(bank,day){return ['oab','geral'].flatMap(mode=>bank.filter(i=>i.mode===mode&&(mode!=='oab'||i.question.editorialStatus==='revisado')).sort((a,b)=>hash(day+a.question.id)-hash(day+b.question.id)||a.question.id.localeCompare(b.question.id)).slice(0,5));}
 function mistakes(bank,history){const last=new Map();for(const a of history)last.set(a.id,a);return bank.filter(i=>last.has(i.question.id)&&last.get(i.question.id).correct===false);}
 function score(correct,index){return correct?(ladder[index]||ladder[ladder.length-1]):0;}
 function eliminate(options){return options.map((o,i)=>o.correct?-1:i).filter(i=>i>=0).slice(0,2);}
 function streak(records,today){const dates=new Set(records.map(r=>r.date));let count=0;const d=new Date(today+'T12:00:00');if(!dates.has(dayKey(d)))d.setDate(d.getDate()-1);while(dates.has(dayKey(d))){count++;d.setDate(d.getDate()-1);}return count;}
 function validateBank(bank){
  if(!Array.isArray(bank)||!bank.length)throw Error('BANCO-VAZIO');
  const ids=new Set(),nonempty=s=>typeof s==='string'&&s.trim().length>0;
  for(const item of bank){
   const q=item&&item.question;
   if(!item||!['oab','geral'].includes(item.mode)||!q||!nonempty(q.id)||ids.has(q.id)||!Number.isInteger(q.version)||q.version<1||!nonempty(q.statement)||!nonempty(q.explanation)||!['fácil','médio','difícil'].includes(q.difficulty)||!Array.isArray(q.options)||q.options.length!==4||!q.options.every(nonempty)||new Set(q.options.map(s=>s.trim().toLocaleLowerCase('pt-BR'))).size!==4||!Number.isInteger(q.correctAnswer)||q.correctAnswer<0||q.correctAnswer>3)throw Error('BANCO-QUESTAO-INVALIDA');
   if(item.mode==='oab'&&(!nonempty(q.discipline)||!nonempty(q.subject)||!['autoral','prova_anterior'].includes(q.origin)||!Array.isArray(q.legalReferences)||!q.legalReferences.length||!q.legalReferences.every(nonempty)))throw Error('BANCO-OAB-INVALIDO');
   if(item.mode==='geral'&&!nonempty(q.category))throw Error('BANCO-CATEGORIA-INVALIDA');
   if(q.sourceUrl&&!/^https:\/\//.test(q.sourceUrl))throw Error('BANCO-FONTE-INVALIDA');
   ids.add(q.id);
  }
  return bank;
 }
 return {validateBank,dayKey,daily,mistakes,score,eliminate,streak,ladder};
});
