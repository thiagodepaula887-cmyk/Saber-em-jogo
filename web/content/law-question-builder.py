from pathlib import Path
from collections import Counter,defaultdict,deque
import json,re,hashlib,random,os
p=Path(__file__).resolve().parents[2];src=Path(os.environ.get('QUIZ_LEGAL_SOURCE_DIR',str(p/'.legal-sources')))
laws=[json.loads(f.read_text()) for f in src.glob('*.json') if f.name not in ['catalog-ready.json','catalog.json']]
laws=[l for l in laws if 'articles' in l];byid={l['id']:l for l in laws};items=json.loads((p/'web/dist/questions.json').read_text());items=[i for i in items if not i['question']['id'].startswith(('seca_','phi_','penal_concept_'))]
# Restore original small seed if this script is re-run after expansion.
items=[i for i in items if i['mode']=='geral' or re.match(r'oab_.*_00[1-8]$',i['question']['id'])]
def topic(law,num,text):
 n=int(re.match(r'\d+',num).group());id=law['id']
 ranges={
 'estatuto-oab':[(7,'Atividade e prerrogativas da advocacia'),(14,'Inscrição, estágio e incompatibilidades'),(21,'Sociedades e advogado empregado'),(26,'Honorários'),(33,'Incompatibilidades, impedimentos e ética'),(43,'Infrações e sanções disciplinares'),(67,'Organização da OAB'),(200,'Processos, recursos e disposições gerais')],
 'cp':[(12,'Princípios e aplicação da lei penal'),(31,'Iter criminis e teoria do delito'),(58,'Penas e espécies de sanção'),(76,'Penas, dosimetria e circunstâncias'),(90,'Concurso de crimes e execução'),(120,'Extinção da punibilidade'),(154,'Crimes contra a pessoa'),(183,'Crimes contra o patrimônio'),(234,'Crimes contra a dignidade sexual e outros bens'),(400,'Crimes contra a administração e a fé pública')],
 'cc':[(78,'Pessoas, personalidade e domicílio'),(232,'Negócios jurídicos, prescrição e prova'),(420,'Obrigações e responsabilidade'),(965,'Contratos e responsabilidade civil'),(1195,'Empresa e sociedades'),(1510,'Direitos reais e propriedade'),(1783,'Família'),(9999,'Sucessões')],
 'cpc':[(15,'Normas fundamentais'),(175,'Jurisdição, partes e sujeitos'),(293,'Atos, prazos e formação do processo'),(311,'Tutelas provisórias'),(538,'Procedimento comum, prova e sentença'),(770,'Cumprimento e procedimentos especiais'),(925,'Execução'),(1200,'Tribunais e recursos')],
 'cpp':[(23,'Lei processual e investigação'),(62,'Ação penal'),(112,'Competência e impedimentos'),(250,'Prova e medidas assecuratórias'),(350,'Prisões, liberdade e cautelares'),(405,'Atos, sentença e procedimento'),(550,'Procedimentos especiais e júri'),(700,'Nulidades e recursos'),(1000,'Execução e disposições gerais')],
 'clt':[(200,'Contrato, duração do trabalho e segurança'),(441,'Proteção ao trabalho'),(510,'Contrato individual, remuneração e rescisão'),(625,'Organização sindical e negociação'),(735,'Justiça do Trabalho e competência'),(900,'Processo, prova e recursos trabalhistas'),(9999,'Disposições gerais')],
 'cf':[(4,'Princípios fundamentais'),(17,'Direitos e garantias fundamentais'),(43,'Estado e administração pública'),(75,'Poder Legislativo'),(91,'Poder Executivo'),(135,'Justiça e funções essenciais'),(162,'Tributação'),(169,'Finanças públicas'),(192,'Ordem econômica'),(250,'Ordem social')]
 }
 for limit,label in ranges.get(id,[]):
  if n<=limit:return label
 # Named laws already provide a meaningful thematic subdivision; subgroup by legal range.
 return law['title']+' · '+('Fundamentos e direitos' if n<=15 else 'Regras e procedimentos' if n<=40 else 'Aplicação e garantias' if n<=80 else 'Organização e disposições especiais')
for item in items:
 q=item['question']
 if item['mode']=='oab':
  for law in laws:
   if q.get('sourceUrl')==law['sourceUrl']:
    q['lawId']=law['id'];q['tags']=[law['title'],law['number'],*law['aliases']];break
  q['contentKind']='conceito';q['subject']='Fundamentos e conceitos'
def addq(id,discipline,subject,statement,options,correct,explanation,refs,url,**extra):
 items.append({'mode':'oab','question':dict(id=id,version=1,discipline=discipline,subject=subject,statement=statement,options=options,correctAnswer=correct,explanation=explanation,difficulty='fácil',origin='autoral',legalReferences=refs,sourceUrl=url,sourceAccessedAt='2026-10-21',**extra)})
for i,line in enumerate((p/'web/content/philosophy.tsv').read_text().splitlines()):
 subject,statement,correct,b,c,d,exp,slug=line.split('|');options=[correct,b,c,d];shift=i%4;options=options[-shift:]+options[:-shift] if shift else options
 addq(f'phi_{i+1:03}','Filosofia do Direito',subject,statement,options,shift,exp,['Material conceitual autoral; referência de apoio: Stanford Encyclopedia of Philosophy'],f'https://plato.stanford.edu/entries/{slug}/',contentKind='conceito')
for i,line in enumerate((p/'web/content/penal-concepts.tsv').read_text().splitlines()):
 subject,statement,correct,b,c,d,exp,art=line.split('|');options=[correct,b,c,d];shift=i%4;options=options[-shift:]+options[:-shift] if shift else options
 addq(f'penal_concept_{i+1:03}','Direito Penal',subject,statement,options,shift,exp,[f'Código Penal, art. {art}; explicação conceitual autoral'],byid['cp']['sourceUrl'],lawId='cp',tags=['iter criminis','in bonam partem','in malam partem','dosimetria','atenuantes','majorantes','princípios'] if i<3 else [subject],contentKind='conceito')
# Use curated article ranges for each discipline; do not turn philosophical study into statute questions.
assign={
'Ética Profissional':[('estatuto-oab',0,9999)],'Direito Constitucional':[('cf',1,192)],'Direito Civil':[('cc',1,965),('cc',1196,9999)],'Processo Civil':[('cpc',0,9999)],'Direito Penal':[('cp',1,9999),('execucao-penal',0,9999)],'Processo Penal':[('cpp',0,9999)],'Direito do Trabalho':[('clt',1,625)],'Processo do Trabalho':[('clt',643,9999)],'Direito Administrativo':[('licitacoes',0,9999),('processo-admin',0,9999)],'Direito Tributário':[('ctn',0,9999)],'Direito Empresarial':[('cc',966,1195),('falencias',0,9999)],'Direito do Consumidor':[('cdc',0,9999)],'Estatuto da Criança e do Adolescente':[('eca',0,9999)],'Direito Ambiental':[('crimes-ambientais',0,9999),('pnam',0,9999)],'Direito Internacional':[('migracao',0,9999),('lindb',0,19)],'Direito Eleitoral':[('eleitoral',0,9999),('eleicoes',0,9999)],'Direito Previdenciário':[('beneficios',0,9999)],'Direito Financeiro':[('orcamento',0,9999),('lrf',0,9999)],'Direitos Humanos':[('lbi',0,9999),('cf',1,17)]}
# Literal completion uses whole words from the actual provision; distractors are different words of the same legal-text pool.
rx=re.compile(r'\b(?:não|somente|direito|direitos|dever|deveres|poderá|deverá|será|pessoa|pessoas|advogado|advogados|juiz|juízes|lei|leis|pena|penas|crime|crimes|processo|contrato|trabalho|competência|responsabilidade|liberdade|obrigação|recurso|reclusão|detenção|multa|União|Estado|Município|contribuinte|empregador|empregado|consumidor|fornecedor|criança|adolescente|benefício|segurado|salário|orçamento|imposto|tributo|eleitor|voto|estrangeiro|brasileiro|sociedade|bens|patrimônio|licitação|administração|autoridade|serviço|serviços|público|privado|civil|penal)\b',re.I)
used=set(i['question']['statement'] for i in items)
used_excerpts=set()
all_groups={}

for discipline,allowed in assign.items():
 groups=defaultdict(list)
 for lawid,lo,hi in allowed:
  if lawid not in byid:continue
  law=byid[lawid]
  for article in law['articles']:
   n=int(re.match(r'\d+',article['number']).group())
   if not lo<=n<=hi:continue
   for pi,part in enumerate(article['parts']):
    text=re.sub(r'^(?:Art\.?\s*\d+[ºo°]?(?:-[A-Z])?\s*[-–.]?\s*|§\s*\d+[ºo°]?\s*[-–.]?\s*|Parágrafo único[.\s-]*|[IVXLCDM]+\s*[-–]\s*)','',part).strip()
    if not 90<=len(text)<=800 or '\ufffd' in text or re.search(r'(?i)revogad|vetado|redação anterior',text):continue
    matches=list(rx.finditer(text));
    if not matches:continue
    # Prefer content words over modal verbs if possible.
    substantive=[m for m in matches if len(m.group())>=5];m=(substantive or matches)[0];answer=m.group()
    alternatives=['processo','contrato','direito','dever','pena','multa','lei','trabalho','serviço','Estado','União','pessoa','sociedade','liberdade','obrigação']
    distractors=[w for w in alternatives if w.casefold()!=answer.casefold()]
    rng=random.Random(f'{discipline}-{lawid}-{article["number"]}-{pi}');rng.shuffle(distractors);opts=[answer,*distractors[:3]];rng.shuffle(opts);correct=opts.index(answer)
    prompt=f'Lei seca · {law["title"]} ({law["number"]}), art. {article["number"]}'+(f', trecho {pi+1}' if pi else '')+f'. Complete a redação consultada: “{text[:m.start()]}[___]{text[m.end():]}”'
    if prompt in used or (lawid,text) in used_excerpts:continue
    used_excerpts.add((lawid,text))
    subject=topic(law,article['number'],text);groups[subject].append((law,article,text,prompt,opts,correct,pi));used.add(prompt)
 all_groups[discipline]=groups
# Balance coverage first, then continue through disciplines while legal passages remain.
serial=Counter()
while len(items)<10240 and all_groups:
 for discipline in list(all_groups):
  groups=all_groups[discipline]
  subjects=list(groups)
  subject=subjects[serial[discipline]%len(subjects)]
  law,article,text,prompt,opts,correct,pi=groups[subject].pop(0)
  serial[discipline]+=1
  if not groups[subject]:del groups[subject]
  if not groups:del all_groups[discipline]
  addq(f'seca_{law["id"]}_{hashlib.sha1(discipline.encode()).hexdigest()[:6]}_{article["number"]}_{pi}',discipline,subject,prompt,opts,correct,f'Na redação consultada: “{text}” A alternativa completa literalmente o trecho. Consulte a fonte oficial e eventuais notas de vigência ou decisões judiciais.',[f'{law["title"]}, {law["number"]}, art. {article["number"]}'],law['sourceUrl'],lawId=law['id'],article=article['number'],sourceExcerpt=text,tags=[law['title'],law['number'],*law['aliases'],subject],contentKind='lei_seca')
  if len(items)==10240:break
counts=Counter(i['question']['discipline'] for i in items if i['mode']=='oab');assert len(counts)==20 and min(counts.values())>=50,counts
assert len(items)==10240;assert len({i['question']['id'] for i in items})==10240;assert len({i['question']['statement'] for i in items})==10240
for l in laws:
 for a in l['articles']:a.pop('parts',None)
(p/'web/dist/law-library.json').write_text(json.dumps(laws,ensure_ascii=False,separators=(',',':'))+'\n')
(p/'web/dist/questions.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
report={'total':len(items),'modules':dict(Counter(i['mode'] for i in items)),'categories':dict(counts),'laws':len(laws),'sourceAccessedAt':'2026-10-21','contentKinds':dict(Counter(i['question'].get('contentKind','geral') for i in items)),'sha256':hashlib.sha256((p/'web/dist/questions.json').read_bytes()).hexdigest()}
(p/'web/content/manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
