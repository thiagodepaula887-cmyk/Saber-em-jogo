from pathlib import Path
from collections import Counter
import json,unicodedata,hashlib
root=Path(__file__).resolve().parents[1]
def slug(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn').replace(' ','_')
urls={
'Ética Profissional':'https://www.planalto.gov.br/ccivil_03/leis/l8906.htm',
'Direito Constitucional':'https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm',
'Direito Civil':'https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm',
'Processo Civil':'https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm',
'Direito Penal':'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm',
'Processo Penal':'https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm',
'Direito do Trabalho':'https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm',
'Processo do Trabalho':'https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm',
'Direito Administrativo':'https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm',
'Direito Tributário':'https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm',
'Direito Empresarial':'https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm',
'Direito do Consumidor':'https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm',
'Estatuto da Criança e do Adolescente':'https://www.planalto.gov.br/ccivil_03/leis/l8069.htm',
'Direito Ambiental':'https://www.planalto.gov.br/ccivil_03/leis/l6938.htm',
'Direito Internacional':'https://www.planalto.gov.br/ccivil_03/decreto-lei/del4657compilado.htm'}
urls.update({'Direito Eleitoral':urls['Direito Constitucional'],'Direito Previdenciário':'https://www.planalto.gov.br/ccivil_03/leis/l8213compilado.htm','Direito Financeiro':'https://www.planalto.gov.br/ccivil_03/leis/l4320.htm','Direitos Humanos':urls['Direito Constitucional'],'Filosofia do Direito':'https://www.gutenberg.org/files/8438/8438-h/8438-h.htm'})
def source(ref,cat):
 if ref.startswith('Kant'):return 'https://www.gutenberg.org/files/5682/5682-h/5682-h.htm'
 if ref.startswith('Convenção Americana'):return 'https://www.planalto.gov.br/ccivil_03/decreto/d0678.htm'
 for needle,url in [('Constituição Federal',urls['Direito Constitucional']),('CPP',urls['Processo Penal']),('Lei 11.101','https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11101.htm'),('Lei 9.784','https://www.planalto.gov.br/ccivil_03/leis/l9784.htm'),('Lei 9.985','https://www.planalto.gov.br/ccivil_03/leis/l9985.htm'),('Lei 9.605','https://www.planalto.gov.br/ccivil_03/leis/l9605.htm')]:
  if ref.startswith(needle):return url
 return urls[cat]
items=[]
for mode,filename in [('geral','general.txt'),('oab','oab.txt')]:
 cat='';counts=Counter()
 for line in (root/'content'/filename).read_text().splitlines():
  if not line.strip():continue
  if line.startswith('# '):cat=line[2:];continue
  fields=line.split('|');assert len(fields)==(7 if mode=='oab' else 6),(cat,len(fields),line)
  statement,*rest=fields;options=rest[:4];explanation=rest[4];assert len(set(options))==4
  counts[cat]+=1
  # A posição armazenada também é distribuída; o jogo embaralha novamente em cada rodada.
  shift=(counts[cat]-1)%4;options=options[-shift:]+options[:-shift] if shift else options
  q=dict(id=f'{mode}_{slug(cat)}_{counts[cat]:03}',version=1,subject=cat,statement=statement,options=options,correctAnswer=shift,explanation=explanation,difficulty='fácil')
  if mode=='oab':q.update(discipline=cat,origin='autoral',legalReferences=[fields[6]],sourceUrl=source(fields[6],cat),reviewedAt='2026-10-16')
  else:q['category']=cat
  items.append(dict(mode=mode,question=q))
 assert all(n==(32 if c=='variedades' else 26) if mode=='geral' else n==8 for c,n in counts.items()),dict(counts)
 assert len(counts)==(9 if mode=='geral' else 20),dict(counts)
assert len(items)==400
assert len({i['question']['id'] for i in items})==400
assert len({i['question']['statement'] for i in items})==400
(root/'dist'/'questions.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
report={'total':400,'modules':dict(Counter(i['mode'] for i in items)),'categories':dict(Counter((i['question'].get('discipline') or i['question'].get('category')) for i in items)),'sha256':hashlib.sha256((root/'dist'/'questions.json').read_bytes()).hexdigest()}
(root/'content'/'manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
