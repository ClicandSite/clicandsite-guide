import re,glob,html
from urllib.parse import unquote_plus, quote_plus
M={
"Alpes françaises":"Mont Blanc","Alpes françaises ski":"Chamonix ski","Alpes ski cours":"Chamonix ski","Briançon":"Grenoble",
"Megève":"Mont Blanc","Morzine":"Annecy","Musée Grévin":"Grevin","Menton Italie excursion":"Menton","Menton Roquebrune-Cap-Martin":"Menton",
"Mougins Grasse excursion":"Grasse","Paris Musée du Louvre billet":"Louvre","Paris souterrain visite":"Catacombes Paris",
"Paris illuminations Noël visite":"Paris Christmas lights","Paris illuminations de Noël":"Paris Christmas lights",
"iles d'Hyeres bateau":"Hyères Porquerolles","Strasbourg croisière Batorama":"Strasbourg","Cannes bateau":"Cannes Iles de Lerins",
"Nice visite guidée":"Nice walking tour",
"Briancon":"Grenoble","Megeve":"Mont Blanc","French Alps":"Mont Blanc","French Alps ski":"Chamonix ski","French Alps ski lessons":"Chamonix ski",
"Hyeres islands boat":"Hyères Porquerolles","Paris Palais Garnier":"Opera Garnier","Paris Palais Garnier guided tour":"Opera Garnier",
"Paris Pantheon ticket":"Pantheon Paris","Paris underground tour":"Paris Catacombs","Strasbourg boat cruise":"Strasbourg",
"Mougins Grasse tour":"Grasse","Les Baux-de-Provence":"Carrieres des Lumieres",
}
n=0
for f in glob.glob('/home/claude/clicandsite-guide*/**/*.html',recursive=True):
    s=open(f).read()
    def rep(m):
        global n
        q=unquote_plus(html.unescape(m[2]))
        if q in M: n+=1; return m[1]+quote_plus(M[q])+'&'
        return m[0]
    t=re.sub(r'(viator\.com(?:/fr-FR)?/searchResults/all\?text=)([^&"]*)&',rep,s)
    if t!=s: open(f,'w').write(t)
print(n)
for f in glob.glob('/tmp/gen/data*.py'):
    s=open(f).read(); t=s
    for k,v in M.items(): t=t.replace(f"'{k}'",f"'{v}'")
    if t!=s: open(f,'w').write(t); print('data',f)
