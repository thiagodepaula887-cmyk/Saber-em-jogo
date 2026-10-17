(function(root,factory){const api=factory();if(typeof module==='object'&&module.exports)module.exports=api;else root.QuizEngine=api;})(typeof globalThis!=='undefined'?globalThis:this,function(){
 'use strict';
 const ladder=[100,200,300,500,1000,2000,3000,5000,10000,20000];
 function dayKey(d=new Date()){return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;}
 function hash(s){let n=2166136261;for(const c of s){n^=c.charCodeAt(0);n=Math.imul(n,16777619);}return n>>>0;}
 function daily(bank,day){return ['oab','geral'].flatMap(mode=>bank.filter(i=>i.mode===mode).sort((a,b)=>hash(day+a.question.id)-hash(day+b.question.id)||a.question.id.localeCompare(b.question.id)).slice(0,5));}
 function mistakes(bank,history){const last=new Map();for(const a of history)last.set(a.id,a);return bank.filter(i=>last.has(i.question.id)&&last.get(i.question.id).correct===false);}
 function score(correct,index){return correct?(ladder[index]||ladder[ladder.length-1]):0;}
 function eliminate(options){return options.map((o,i)=>o.correct?-1:i).filter(i=>i>=0).slice(0,2);}
 function streak(records,today){const dates=new Set(records.map(r=>r.date));let count=0;const d=new Date(today+'T12:00:00');if(!dates.has(dayKey(d)))d.setDate(d.getDate()-1);while(dates.has(dayKey(d))){count++;d.setDate(d.getDate()-1);}return count;}
 return {dayKey,daily,mistakes,score,eliminate,streak,ladder};
});
