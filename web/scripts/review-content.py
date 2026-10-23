#!/usr/bin/env python3
"""Build v9 preserving all original questions and clearly labeling pending review."""
from pathlib import Path
import gzip,json,runpy,hashlib,collections
root=Path(__file__).resolve().parents[1]
old=json.loads(gzip.decompress((root/'content/questions.v7.json.gz').read_bytes()))
laws=json.loads(gzip.decompress((root/'content/law-library.v7.json.gz').read_bytes())); lawmap={l['id']:l for l in laws}
rows=runpy.run_path(str(root/'content/casos-revisados.py'))['ROWS'].splitlines(); new=[]
for n,row in enumerate(rows):
 d,subject,lid,refs,statement,correct,b,c,e,exp=row.split('|')
 options=[correct,b,c,e];shift=n%4;options=options[-shift:]+options[:-shift] if shift else options
 law=lawmap[lid];theory=d=='Filosofia do Direito'
 q=dict(id=f'caso_v8_{n+1:03}',version=1,discipline=d,subject=subject,lawId=lid if not theory else '',statement=statement,options=options,correctAnswer=shift,explanation=exp,difficulty='difícil' if n%2==0 else 'médio',origin='autoral',contentKind='caso_juridico',editorialStatus='revisado',difficultyBasis='Estimativa editorial: aplicação de regra, distinção entre institutos e distratores jurídicos; não calibrada por desempenho.',legalReferences=[refs if theory else f'{law["title"]}, art. {refs}'],sourceUrl='https://plato.stanford.edu/entries/legal-positivism/' if theory and n%2==0 else 'https://plato.stanford.edu/entries/kant-moral/' if theory else law['sourceUrl'],sourceAccessedAt='2026-10-22',reviewedAt='2026-10-22',tags=[subject] if theory else [law['title'],law['number'],*law['aliases'],subject])
 if not theory:
  import re
  article=re.match(r'\d+',refs).group();a=next((a for a in law['articles'] if a['number']==article),None)
  assert a,(lid,article)
  q['article']=article
 new.append({'mode':'oab','question':q})
assert len(new)==40 and len({i['question']['discipline'] for i in new})==20
# Preserve every original question; pending review is metadata, never a deletion rule.
base=[];audit=[]
for item in old:
 q=item['question']
 if item['mode']=='geral':base.append(item);continue
 bad=q.get('contentKind')=='lei_seca'
 audit.append({'id':q['id'],'decision':'preservado_pendente' if bad else 'basico_pendente','reason':'Lacuna com distratores de classes gramaticais e domínios incompatíveis; exige substituição editorial.' if bad else 'Pergunta introdutória com distratores evidentes; não classificada como treino exigente. Revisão jurídica individual não concluída.'})
 q['editorialStatus']='revisao_pendente' if bad else 'basico_pendente'
 base.append(item)
bank=base+new; raw=(json.dumps(bank,ensure_ascii=False,indent=2)+'\n').encode()
(root/'content/questions.v9.json.gz').write_bytes(gzip.compress(raw,mtime=0))
report={'version':9,'date':'2026-10-22','audited':len(audit),'withdrawn':sum(a['decision']=='retirado' for a in audit),'basicPending':sum(a['decision']=='basico_pendente' for a in audit),'newCases':len(new),'defaultLegalPool':sum(i['mode']=='oab' for i in bank),'activeLegalTotal':sum(i['mode']=='oab' for i in bank),'total':len(bank),'legalReviewComplete':False,'questions':audit}
(root/'content/editorial-audit.v9.json.gz').write_bytes(gzip.compress((json.dumps(report,ensure_ascii=False)+'\n').encode(),mtime=0))
manifest={'version':9,'total':len(bank),'modules':dict(collections.Counter(i['mode'] for i in bank)),'categories':dict(collections.Counter(i['question']['discipline'] for i in bank if i['mode']=='oab')),'laws':len(laws),'contentKinds':dict(collections.Counter(i['question'].get('contentKind','geral') for i in bank)),'sha256':hashlib.sha256(raw).hexdigest(),'editorial':{k:v for k,v in report.items() if k!='questions'}}
(root/'content/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='questions'},ensure_ascii=False))
