import React, {useEffect,useRef,useState} from 'react';
import {ScrollView,Text,Pressable,View,StyleSheet,Alert} from 'react-native';
import {QuizQuestion,OptionIndex} from '../types/quiz';
import {repository} from '../database/db';
interface Props {sessionId:string;items:QuizQuestion[];onFinish:(r:{score:number;total:number})=>void;onExit:()=>void;}
export default function QuizScreen({sessionId,items,onFinish,onExit}:Props){
 const [index,setIndex]=useState(0);const [selected,setSelected]=useState<OptionIndex|null>(null);
 const [correct,setCorrect]=useState(false);const [error,setError]=useState('');
 const answered=useRef(false);const advancing=useRef(false);const finished=useRef(false);const scroll=useRef<React.ComponentRef<typeof ScrollView>>(null);
 useEffect(()=>{advancing.current=false;answered.current=false;scroll.current?.scrollTo({y:0,animated:false});},[index]);
 const item=items[index];if(!item)return <Text>Nenhuma questão disponível.</Text>;
 const q=item.question;
 const label=item.mode==='oab'?item.question.discipline:item.question.category;
 function select(option:OptionIndex){
  if(answered.current || advancing.current || finished.current)return;
  answered.current=true;setError('');
  try{const ok=repository.answer(sessionId,q.id,q.version,option);setCorrect(ok);setSelected(option);}
  catch{answered.current=false;setError('Não foi possível salvar. Toque na alternativa para tentar novamente.');}
 }
 function next(){
  if(!answered.current || selected===null || advancing.current || finished.current)return;
  advancing.current=true;
  if(index+1<items.length){setSelected(null);setError('');setIndex(i=>i+1);}
  else{try{const result=repository.finish(sessionId);finished.current=true;onFinish(result);}catch{advancing.current=false;setError('Não foi possível concluir. Tente novamente.');}}
 }
 return <ScrollView ref={scroll} contentContainerStyle={s.page}>
  <Pressable accessibilityRole="button" onPress={()=>Alert.alert('Sair da partida?','As respostas já registradas permanecem no histórico.',[{text:'Continuar',style:'cancel'},{text:'Sair',onPress:onExit}])}><Text style={s.muted}>‹ Sair da partida</Text></Pressable>
  <Text style={s.tag}>{label} · {q.difficulty}</Text>
  <Text style={s.muted}>QUESTÃO {index+1} DE {items.length}</Text>
  <View style={s.track}><View style={[s.fill,{width:`${((index+1)/items.length)*100}%`}]}/></View>
  <Text style={s.statement}>{q.statement}</Text>
  {q.options.map((option,i)=><Pressable key={i} accessibilityRole="button" accessibilityState={{disabled:selected!==null,selected:selected===i}} disabled={selected!==null} onPress={()=>select(i as OptionIndex)} style={[s.option,selected!==null&&i===q.correctAnswer?s.right:null,selected===i&&i!==q.correctAnswer?s.wrong:null]}>
   <Text style={s.optionText}>{String.fromCharCode(65+i)}   {option}{selected!==null&&i===q.correctAnswer?'  ✓':''}</Text>
  </Pressable>)}
  {!!error&&<Text accessibilityRole="alert" style={s.error}>{error}</Text>}
  {selected!==null&&<View style={s.comment}>
   <Text accessibilityLiveRegion="polite" style={s.feedback}>{correct?'✓ Resposta correta!':'↻ Vamos aprender com essa'}</Text>
   <Text style={s.tag}>{item.mode==='oab'?'COMENTÁRIO JURÍDICO':'EXPLICAÇÃO'}</Text>
   <Text style={s.body}>{q.explanation}</Text>
   {item.mode==='oab'&&item.question.legalReferences.map(r=><Text key={r} style={s.muted}>{r}</Text>)}
   <Pressable accessibilityRole="button" style={s.button} onPress={next}><Text style={s.buttonText}>{index+1===items.length?'Ver resultado':'Próxima questão →'}</Text></Pressable>
  </View>}
 </ScrollView>;
}
const s=StyleSheet.create({page:{padding:24,paddingBottom:48,backgroundColor:'#10172b',flexGrow:1},muted:{color:'#b4bed3',fontSize:13,lineHeight:20},tag:{color:'#a7f3d0',fontWeight:'700',marginVertical:16,fontSize:13},track:{height:6,backgroundColor:'#29324a',borderRadius:5,marginTop:12},fill:{height:6,backgroundColor:'#65e6bb',borderRadius:5},statement:{color:'#fff',fontSize:23,lineHeight:33,fontWeight:'700',marginVertical:26},option:{backgroundColor:'#1b2540',borderWidth:1,borderColor:'#35415b',padding:18,borderRadius:16,marginBottom:12,minHeight:58},optionText:{color:'#fff',fontSize:16,lineHeight:24},right:{borderColor:'#65e6bb',backgroundColor:'#154b43'},wrong:{borderColor:'#ff99a4',backgroundColor:'#512c3c'},comment:{padding:20,backgroundColor:'#1b2540',borderRadius:20,marginTop:12},feedback:{color:'#fff',fontWeight:'700',fontSize:19},body:{color:'#e3e8f1',fontSize:16,lineHeight:25,marginBottom:16},button:{backgroundColor:'#65e6bb',padding:18,borderRadius:14,marginTop:22,alignItems:'center'},buttonText:{color:'#102b28',fontSize:16,fontWeight:'800'},error:{color:'#ffc1c8',padding:14}});
