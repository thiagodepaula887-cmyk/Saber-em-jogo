const {test}=require('node:test'),a=require('node:assert/strict'),vm=require('node:vm'),fs=require('node:fs');
const bank=require('../dist/questions.json');
async function boot({getItem=()=>null,setItem=()=>{},data=bank,networkError=false}={}){
 const nodes=new Map(),root={dataset:{},innerHTML:'',querySelectorAll:()=>[]},node=id=>{if(!nodes.has(id))nodes.set(id,{});return nodes.get(id);};
 const c={document:{getElementById:id=>id==='app'?root:node(id)},window:{scrollTo(){}},localStorage:{getItem,setItem},confirm:()=>true,fetch:async()=>{if(networkError)throw Error('offline');return {ok:true,json:async()=>data};},setInterval:()=>1,clearInterval(){}};
 vm.createContext(c);for(const file of ['game-engine.js','app.js'])vm.runInContext(fs.readFileSync('dist/'+file,'utf8'),c);await new Promise(setImmediate);return {c,root,node};
}
test('falha de carga mostra diagnóstico e recuperação',async()=>{const {root}=await boot({networkError:true});a.equal(root.dataset.error,'BANCO-CARGA');a(root.innerHTML.includes('Tentar novamente'));a.notEqual(root.dataset.ready,'1');});
test('banco duplicado não inicia partida parcial',async()=>{const {root}=await boot({data:[bank[0],bank[0]]});a.equal(root.dataset.error,'BANCO-CARGA');a.notEqual(root.dataset.ready,'1');});
test('armazenamento bloqueado permite jogar com aviso',async()=>{const {root,c}=await boot({getItem:()=>{throw Error('denied')},setItem:()=>{throw Error('denied')}});a.equal(root.dataset.ready,'1');a(root.innerHTML.includes('Progresso apenas nesta sessão'));vm.runInContext("mode='geral';playStyle='study';start();answer(0)",c);a.equal(vm.runInContext('history.length',c),1);});
test('histórico corrompido permite abrir a capa',async()=>{const {root}=await boot({getItem:()=>'{bad json'});a.equal(root.dataset.ready,'1');});
test('histórico válido é carregado após reabertura',async()=>{const saved={id:bank[0].question.id,version:1,correct:true,at:Date.now()};const {c}=await boot({getItem:key=>key==='saber-history-v1'?JSON.stringify([saved]):null});a.equal(vm.runInContext('history.length',c),1);});
