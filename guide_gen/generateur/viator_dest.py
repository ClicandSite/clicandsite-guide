import re,sys,os,glob
P='Paris/d479'
M={'chamonix+mont+blanc':'Chamonix/d24269','chamonix+aiguille+du+midi':'Chamonix/d24269','courchevel':'Rhone-Alpes/d24268',
'mont+saint+michel':'Mont-St-Michel/d25906','grand+prix+de+monaco':'Monaco/d948','casino+monte+carlo':'Monaco/d948','monaco+rocher':'Monaco/d948',
'fete+du+citron+menton':'Menton/d23076','lemon+festival+menton':'Menton/d23076','lascaux':'Bergerac/d24181','dune+du+pilat':'Arcachon/d26516',
'cap+d+antibes':'Antibes/d21941','remparts+d+antibes':'Antibes/d21941','palace+of+versailles':'Versailles/d763',
'festival+de+cannes':'Cannes/d786','cannes+lerins+islands':'Cannes/d786','nice+food+tour':'Nice/d478','nice+castle+hill':'Nice/d478','castle+hill+nice':'Nice/d478',
'musee+chagall+nice':'Nice/d478','nice+promenade+des+anglais':'Nice/d478','marseille+notre+dame+de+la+garde':'Marseille/d485',
'blois+chateau+de+chambord':'Loire-Valley/d178','bayeux+d+day+landing+beaches':'Bayeux/d909','bayeux+omaha+beach':'Bayeux/d909',
'avignon+palais+des+papes':'Avignon/d483','palais+des+papes':'Avignon/d483','biarritz+aquarium':'Biarritz/d23856','arles+amphitheatre':'Arles/d28884',
'rennes+saint+malo+ramparts':'Rennes/d21943'}
pat=re.compile(r'https://www\.viator\.com/((?:[a-z]{2}-[A-Z]{2}/)?)searchResults/all\?text=([^&"\']+)(&amp;|&)')
miss=set();n=0
for repo in sys.argv[1:]:
  for f in glob.glob(repo+'/**/*.html',recursive=True):
    s=open(f).read()
    if 'searchResults' not in s: continue
    def rep(m):
      global n
      t=m.group(2).lower(); d=M.get(t) or (P if t.startswith('paris+') or t.endswith('+paris') or t in('louvre','montmartre','pere+lachaise+cemetery','louis+vuitton+foundation','pantheon+paris','picasso+museum+paris') else None)
      if not d: miss.add(t); return m.group(0)
      n+=1; return f'https://www.viator.com/{m.group(1)}{d}-ttd?'
    s2=pat.sub(rep,s)
    if s2!=s: open(f,'w').write(s2)
print(n,'remplacés; manquants:',miss)
