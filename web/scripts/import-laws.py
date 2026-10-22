from pathlib import Path
import json,urllib.request,concurrent.futures,re,hashlib,sys

from bs4 import BeautifulSoup
from html.parser import HTMLParser
P='https://www.planalto.gov.br/ccivil_03/'
rows=[
('estatuto-oab','Estatuto da Advocacia e da OAB','8.906/1994','leis/l8906.htm',['Ética Profissional'],['8906','890694','lei 8906/94','estatuto da oab','EOAB']),
('cf','Constituição Federal','CF/1988','constituicao/constituicaocompilado.htm',['Direito Constitucional','Direitos Humanos'],['constituição','cf88']),
('cc','Código Civil','10.406/2002','leis/2002/l10406compilada.htm',['Direito Civil','Direito Empresarial'],['codigo civil','CC']),
('cpc','Código de Processo Civil','13.105/2015','_ato2015-2018/2015/lei/l13105.htm',['Processo Civil'],['CPC','novo cpc']),
('cp','Código Penal','2.848/1940','decreto-lei/del2848compilado.htm',['Direito Penal'],['CP','direito penal']),
('cpp','Código de Processo Penal','3.689/1941','decreto-lei/del3689compilado.htm',['Processo Penal'],['CPP']),
('clt','Consolidação das Leis do Trabalho','5.452/1943','decreto-lei/del5452.htm',['Direito do Trabalho','Processo do Trabalho'],['CLT']),
('licitacoes','Lei de Licitações e Contratos Administrativos','14.133/2021','_ato2019-2022/2021/lei/l14133.htm',['Direito Administrativo'],['licitações','14133']),
('ctn','Código Tributário Nacional','5.172/1966','leis/l5172compilado.htm',['Direito Tributário'],['CTN']),
('cdc','Código de Defesa do Consumidor','8.078/1990','leis/l8078compilado.htm',['Direito do Consumidor'],['CDC','consumidor']),
('eca','Estatuto da Criança e do Adolescente','8.069/1990','leis/l8069.htm',['Estatuto da Criança e do Adolescente'],['ECA']),
('crimes-ambientais','Lei de Crimes Ambientais','9.605/1998','leis/l9605.htm',['Direito Ambiental'],['crimes ambientais']),
('pnam','Política Nacional do Meio Ambiente','6.938/1981','leis/l6938.htm',['Direito Ambiental'],['PNMA','meio ambiente']),
('migracao','Lei de Migração','13.445/2017','_ato2015-2018/2017/lei/l13445.htm',['Direito Internacional'],['migração','estrangeiro']),
('lindb','Lei de Introdução às Normas do Direito Brasileiro','4.657/1942','decreto-lei/del4657compilado.htm',['Direito Internacional','Direito Administrativo'],['LINDB']),
('eleitoral','Código Eleitoral','4.737/1965','leis/l4737compilado.htm',['Direito Eleitoral'],['eleitoral']),
('eleicoes','Lei das Eleições','9.504/1997','leis/l9504.htm',['Direito Eleitoral'],['eleições']),
('beneficios','Planos de Benefícios da Previdência Social','8.213/1991','leis/l8213cons.htm',['Direito Previdenciário'],['INSS','benefícios','previdência']),
('orcamento','Normas Gerais de Direito Financeiro','4.320/1964','leis/l4320.htm',['Direito Financeiro'],['orçamento','4320']),
('lrf','Lei de Responsabilidade Fiscal','LC 101/2000','leis/lcp/lcp101.htm',['Direito Financeiro'],['LRF','responsabilidade fiscal']),
('falencias','Lei de Recuperação Judicial e Falências','11.101/2005','_ato2004-2006/2005/lei/l11101.htm',['Direito Empresarial'],['falências','recuperação judicial']),
('lbi','Lei Brasileira de Inclusão','13.146/2015','_ato2015-2018/2015/lei/l13146.htm',['Direitos Humanos'],['LBI','pessoa com deficiência']),
('processo-admin','Processo Administrativo Federal','9.784/1999','leis/l9784.htm',['Direito Administrativo'],['processo administrativo']),
('execucao-penal','Lei de Execução Penal','7.210/1984','leis/l7210.htm',['Direito Penal'],['LEP','execução penal']),
('maria-penha','Lei Maria da Penha','11.340/2006','_ato2004-2006/2006/lei/l11340.htm',['Direito Penal','Processo Penal'],['maria da penha','violência doméstica'])]
class Parser(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.lines=[];self.buf=[];self.stack=[];self.skip=0
 def flush(self):
  t=re.sub(r'\s+',' ',''.join(self.buf)).strip();self.buf=[]
  if t:self.lines.append(t)
 def handle_starttag(self,tag,attrs):
  at=dict(attrs);skip=tag in ['s','strike','del','script','style'] or 'line-through' in at.get('style','').lower()
  if tag in ['p','h1','h2','h3','h4','div','br']:self.flush()
  if tag not in ['br','meta','link','img','hr','input']:
   self.stack.append((tag,skip));self.skip+=int(skip)
 def handle_endtag(self,tag):
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:
    self.skip-=sum(int(x[1]) for x in self.stack[i:]);self.stack=self.stack[:i];break
  if tag in ['p','h1','h2','h3','h4','div']:self.flush()
 def handle_data(self,data):
  if not self.skip:self.buf.append(data)
def clean(t):
 # Remove editorial amendment references, preserving substantive legal parentheses.
 t=re.sub(r'\((?:Reda[çc][ãa]o|Inclu[íi]do|Acrescentado|Renumerado|Vide|Vig[êe]ncia|Produ[çc][ãa]o de efeito|Regulamento|Revogado)[^)]*\)','',t,flags=re.I)
 return re.sub(r'\s+',' ',t).strip()
def work(row):
 id,title,number,path,disc,aliases=row;url=P+path;dest=Path(__file__).resolve().parents[2]/'.legal-sources';dest.mkdir(exist_ok=True)
 for attempt in range(3):
  try:
   b=(dest/f'{id}.html').read_bytes() if (dest/f'{id}.html').exists() else urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=15).read();encoding='utf-8' if b'charset="utf-8"' in b.lower() or b'charset=utf-8' in b.lower() else 'cp1252'
   try:t=b.decode('utf-8') if (dest/f'{id}.html').exists() else b.decode(encoding)
   except UnicodeDecodeError:t=b.decode('latin1')
   soup=BeautifulSoup(t,'html5lib')
   for tag in soup.find_all(['s','strike','del','script','style']):tag.decompose()
   for tag in soup.find_all(style=lambda s:s and 'line-through' in s.lower()):tag.decompose()
   parser=Parser();parser.lines=[node.get_text(' ',strip=True) for node in soup.find_all(['p','h1','h2','h3','h4'])];arts={};current=None
   for raw in parser.lines:
    if id=='cf' and len(arts)>100 and raw.strip().upper().startswith('ATO DAS DISPOSI') and 'TRANSIT' in raw.upper():break
    line=clean(raw)
    line=re.sub(r'^(Art\.?\s*)(\d)\.(\d{3})',r'\1\2\3',line)
    m=re.match(r'^(?:Art\.?|Artigo)\s*(\d+)(?:\s*[ºo°])?(?:\s*[-–]([A-Z])(?=[º°\s.:-]|$))?',line,re.I)
    if m:
     n=m.group(1)+(('-'+m.group(2).upper()) if m.group(2) else '');current=n
     if not re.search(r'\b(?:revogado|vetado)\b',line,re.I):arts[n]={'number':n,'parts':[line]}
     else:current=None
    elif current and line and re.match(r'^(?:§|Par[áa]grafo|[IVXLCDM]+\s*[-–]|[a-z]\))',line):
     if not re.search(r'\b(?:revogado|vetado)\b',line,re.I):arts[current]['parts'].append(line)
   assert len(arts)>8,(id,len(arts))
   result=dict(id=id,title=title,number=number,sourceUrl=url,disciplines=disc,aliases=aliases,accessedAt='2026-10-21',sourceSha256=hashlib.sha256(b).hexdigest(),articles=[dict(number=a['number'],text='\n'.join(a['parts']),parts=a['parts']) for a in arts.values()])
   (dest/f'{id}.html').write_text(t)
   (dest/f'{id}.json').write_text(json.dumps(result,ensure_ascii=False));return result
  except Exception as e:
   print(id,attempt,str(e),flush=True)
   if attempt==2:return {'error':str(e),'id':id}
rows=[r for r in rows if r[0]!='maria-penha']
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:all=list(ex.map(work,rows))
(Path(__file__).resolve().parents[2]/'.legal-sources/catalog-ready.json').write_text(json.dumps(all,ensure_ascii=False))
print([(x['id'],len(x.get('articles',[])),x.get('error','')) for x in all])
