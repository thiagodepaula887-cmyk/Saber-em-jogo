import React,{useEffect,useRef,useState} from 'react';
import {View,Text,ScrollView,Pressable,StyleSheet,StatusBar} from 'react-native';
import {SafeAreaProvider,SafeAreaView} from 'react-native-safe-area-context';
import * as Crypto from 'expo-crypto';
import {repository} from './src/database/db';
import {seed} from './src/data/seed';
import {AppMode,QuizQuestion,categories} from './src/types/quiz';
import QuizScreen from './src/screens/QuizScreen';
function shuffle<T>(items:T[]){const a=[...items];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
export default function App(){return <SafeAreaProvider><SafeAreaView style={{flex:1,backgroundColor:'#10172b'}}><StatusBar barStyle="light-content"/><Main/></SafeAreaView></SafeAreaProvider>;}
function Main(){
 const [ready,setReady]=useState(false);const [error,setError]=useState('');const [mode,setMode]=useState<AppMode|null>(null);
 const [session,setSession]=useState<{id:string;items:QuizQuestion[]}|null>(null);
 const [result,setResult]=useState<{score:number;total:number}|null>(null);
 const [stats,setStats]=useState({total:0,correct:0});const starting=useRef(false);
 function initialize(){try{repository.init();repository.importBatch(seed);setStats(repository.stats());setReady(true);setError('');}catch{setError('Não foi possível abrir o banco local. Tente novamente.');}}
 useEffect(()=>{initialize();},[]);
 function home(){setSession(null);setResult(null);setMode(null);starting.current=false;setStats(repository.stats());}
 function start(category?:string){if(!mode||starting.current)return;starting.current=true;try{const items=shuffle(repository.list(mode,category)).slice(0,10);const id=Crypto.randomUUID();repository.createSession(id,items);setSession({id,items});setError('');}catch{starting.current=false;setError('Não foi possível iniciar a partida. Tente novamente.');}}
 if(session&&!result)return <QuizScreen key={session.id} sessionId={session.id} items={session.items} onExit={home} onFinish={r=>{setResult(r);setStats(repository.stats());}}/>;
 return <ScrollView contentContainerStyle={s.page}>
  <Text style={s.logo}>✦ SABER EM JOGO</Text><Text style={s.kicker}>APRENDA. JOGUE. EVOLUA.</Text>
  {!ready?<><Text style={s.title}>Vamos começar?</Text><Text style={s.body}>{error||'Preparando seu espaço de aprendizado…'}</Text>{!!error&&<Button label="Tentar novamente" onPress={initialize}/>}</>:result?<>
   <Text style={s.heroIcon}>{result.score/result.total>=0.7?'🏆':'🌱'}</Text><Text style={s.title}>Cada pergunta conta.</Text>
   <Text style={s.big}>{result.score}<Text style={s.subtitle}> / {result.total}</Text></Text><Text style={s.body}>acertos nesta partida · {Math.round(result.score/result.total*100)}% de aproveitamento</Text>
   <View style={s.panel}><Text style={s.panelTitle}>+{result.score*10} XP conquistados</Text><Text style={s.body}>Revise os comentários e continue praticando para fixar o conteúdo.</Text></View>
   <Button label="Voltar ao início" onPress={home}/>
  </>:mode?<>
   <Pressable accessibilityRole="button" onPress={()=>{setMode(null);setError('');}}><Text style={s.link}>‹ Voltar</Text></Pressable>
   <Text style={s.title}>{mode==='oab'?'Sua próxima aprovação começa aqui.':'Siga sua curiosidade.'}</Text>
   <Text style={s.body}>Escolha um tema ou misture tudo. Rodadas de até 10 perguntas.</Text>
   <Button label="Jogar todos os temas →" onPress={()=>start()}/>
   {(mode==='geral'?categories:[...new Set(repository.list('oab').map(i=>i.mode==='oab'?i.question.discipline:''))]).map((c,i)=><Pressable accessibilityRole="button" style={s.category} key={c} onPress={()=>start(c)}><Text style={s.categoryText}>{String(i+1).padStart(2,'0')}   {c}</Text><Text style={s.link}>→</Text></Pressable>)}
  </>:<>
   <Text style={s.title}>Conhecimento que vira conquista.</Text><Text style={s.body}>Uma pergunta por vez. Escolha sua jornada e coloque a mente em jogo.</Text>
   <View style={s.stats}><View><Text style={s.panelTitle}>{stats.correct*10} XP</Text><Text style={s.small}>Nível {Math.floor(stats.correct/10)+1}</Text></View><View><Text style={s.panelTitle}>{stats.total?Math.round(stats.correct/stats.total*100):0}%</Text><Text style={s.small}>de acertos</Text></View><View><Text style={s.panelTitle}>{stats.total}</Text><Text style={s.small}>respostas</Text></View></View>
   <Pressable accessibilityRole="button" style={[s.card,s.oab]} onPress={()=>setMode('oab')}><Text style={s.icon}>⚖</Text><Text style={s.badge}>FOCO NA APROVAÇÃO</Text><Text style={s.cardTitle}>Preparatório OAB</Text><Text style={s.body}>Pratique disciplinas jurídicas e entenda o fundamento de cada resposta.</Text><Text style={s.cta}>Começar a estudar →</Text></Pressable>
   <Pressable accessibilityRole="button" style={[s.card,s.general]} onPress={()=>setMode('geral')}><Text style={s.icon}>✺</Text><Text style={s.badge}>EXPLORE 9 CATEGORIAS</Text><Text style={s.cardTitle}>Conhecimentos gerais</Text><Text style={s.body}>De esportes a literatura: descubra algo novo em cada rodada.</Text><Text style={s.cta}>Quero jogar →</Text></Pressable>
   <View style={s.panel}><Text style={s.panelTitle}>Seu aprendizado vai com você</Text><Text style={s.body}>Jogue offline. Seu histórico fica salvo neste aparelho.</Text></View>
   <Text style={s.small}>MVP de demonstração · 400 questões autorais · sem vínculo com OAB ou FGV. Excluir o aplicativo remove os dados locais.</Text>
  </>}
  {!!error&&ready&&<Text accessibilityRole="alert" style={s.error}>{error}</Text>}
 </ScrollView>;
}
function Button({label,onPress}:{label:string;onPress:()=>void}){return <Pressable accessibilityRole="button" style={s.button} onPress={onPress}><Text style={s.buttonText}>{label}</Text></Pressable>;}
const s=StyleSheet.create({page:{padding:24,paddingBottom:48,maxWidth:720,width:'100%',alignSelf:'center'},logo:{color:'#65e6bb',fontWeight:'900',fontSize:18,letterSpacing:2,marginVertical:12},kicker:{color:'#a0aec7',fontSize:10,letterSpacing:2,marginBottom:25},title:{color:'#fff',fontSize:34,lineHeight:41,fontWeight:'800',marginVertical:12},body:{color:'#c5cee0',fontSize:16,lineHeight:25},stats:{flexDirection:'row',justifyContent:'space-between',backgroundColor:'#1b2540',padding:20,borderRadius:20,marginVertical:24},small:{color:'#9caac3',fontSize:12,lineHeight:19},panelTitle:{color:'#fff',fontSize:18,fontWeight:'700',marginBottom:6},card:{padding:24,borderWidth:1,borderRadius:24,marginBottom:18},oab:{backgroundColor:'#183b3d',borderColor:'#31625b'},general:{backgroundColor:'#302848',borderColor:'#514468'},icon:{fontSize:35,color:'#fff',marginBottom:15},badge:{color:'#b7e8dd',fontSize:10,letterSpacing:1.5,fontWeight:'800'},cardTitle:{color:'#fff',fontSize:25,fontWeight:'800',marginVertical:10},cta:{color:'#a7f3d0',fontWeight:'800',fontSize:16,marginTop:22},panel:{backgroundColor:'#1b2540',padding:20,borderRadius:20,marginVertical:20},button:{backgroundColor:'#65e6bb',padding:19,borderRadius:15,marginVertical:22,alignItems:'center'},buttonText:{color:'#102b28',fontSize:16,fontWeight:'800'},link:{color:'#a7f3d0',fontSize:16,marginVertical:10},category:{flexDirection:'row',alignItems:'center',justifyContent:'space-between',padding:18,backgroundColor:'#1b2540',borderRadius:16,marginBottom:10},categoryText:{color:'#fff',fontSize:16,textTransform:'capitalize',flex:1},heroIcon:{fontSize:60,marginTop:20},big:{color:'#65e6bb',fontSize:80,fontWeight:'900',marginTop:24},subtitle:{fontSize:32,color:'#b4bed3'},error:{color:'#ffc1c8',marginVertical:14}});
