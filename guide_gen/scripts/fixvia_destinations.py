import re,glob,html
from urllib.parse import urlparse,parse_qs
D={'Paris':479,'Versailles':763,'Fontainebleau':50925,'Marne-la-Vallee':5637,'Nice':478,'Cannes':786,'Antibes':21941,'Menton':23076,
'Monte-Carlo':50269,'Villefranche-sur-Mer':50322,'St-Tropez':4195,'Grasse':50323,'Frejus-Saint-Raphael':5223,'Moustiers-Sainte-Marie':26221,
'Toulon':24308,'Chamonix':24269,'Annecy':5437,'Rhone-Alpes':24268,'Grenoble':27067,'Perpignan':26343,'Lourdes':24041,'Mont-St-Michel':25906,
'Le-Havre':4199,'Honfleur':50416,'Rouen':5089,'Bayeux':909,'Tours':5092,'Blois':50324,'Aix-en-Provence':5228,'Avignon':483,
'Saint-Remy-de-Provence':50327,'Cassis':50415,'Gordes':50932,'Marseille':485,'Strasbourg':5502,'Colmar':22940}
# slug (last path part, same FR/EN where possible) -> destination
S={'versailles':'Versailles','fontainebleau':'Fontainebleau','disneyland-paris':'Marne-la-Vallee',
'nice':'Nice','carnaval-de-nice':'Nice','eze':'Nice','saint-paul-de-vence':'Nice','noel-cote-d-azur':'Nice','isola-2000':'Nice','auron':'Nice',
'cannes':'Cannes','iles-de-lerins':'Cannes','mougins':'Cannes','antibes':'Antibes','biot':'Antibes',
'menton':'Menton','fete-du-citron-menton':'Menton','roquebrune-cap-martin':'Menton','monaco':'Monte-Carlo',
'villefranche-sur-mer':'Villefranche-sur-Mer','saint-jean-cap-ferrat':'Villefranche-sur-Mer','saint-tropez':'St-Tropez',
'grasse':'Grasse','gourdon':'Grasse','massif-de-l-esterel':'Frejus-Saint-Raphael','gorges-du-verdon':'Moustiers-Sainte-Marie','porquerolles':'Toulon',
'chamonix':'Chamonix','megeve':'Chamonix','la-clusaz':'Annecy','avoriaz':'Rhone-Alpes','chatel':'Rhone-Alpes',
'courchevel':'Rhone-Alpes','meribel':'Rhone-Alpes','les-menuires':'Rhone-Alpes','val-thorens':'Rhone-Alpes','tignes':'Rhone-Alpes','val-d-isere':'Rhone-Alpes','les-arcs':'Rhone-Alpes','la-plagne':'Rhone-Alpes',
'alpe-d-huez':'Grenoble','les-2-alpes':'Grenoble','serre-chevalier':'Grenoble','montgenevre':'Grenoble','la-grave':'Grenoble','superdevoluy':'Grenoble',
'font-romeu':'Perpignan','saint-lary':'Lourdes','grand-tourmalet':'Lourdes','cauterets':'Lourdes','peyragudes':'Lourdes',
'mont-saint-michel':'Mont-St-Michel','etretat':'Le-Havre','honfleur':'Honfleur','rouen':'Rouen','plages-du-debarquement':'Bayeux','d-day-beaches':'Bayeux',
'amboise':'Tours','chenonceau':'Tours','villandry':'Tours','chambord':'Blois',
'aix-en-provence':'Aix-en-Provence','avignon':'Avignon','baux-de-provence':'Saint-Remy-de-Provence','calanques':'Cassis','gordes':'Gordes','marseille':'Marseille',
'nice-carnival':'Nice','christmas-french-riviera':'Nice','lerins-islands':'Cannes','verdon-gorge':'Moustiers-Sainte-Marie','esterel-massif':'Frejus-Saint-Raphael','lemon-festival-menton':'Menton','strasbourg':'Strasbourg','colmar':'Colmar','kaysersberg':'Colmar','riquewihr':'Colmar',
'cote-d-azur-en-hiver':'Nice','french-riviera-in-winter':'Nice','stations-de-ski-ouvertes':'Chamonix','ski-resort-opening-dates':'Chamonix'}
miss=set(); n=0
for root,lang in (('clicandsite-guide','fr'),('clicandsite-guide-en','en')):
    for f in glob.glob(root+'/**/index.html',recursive=True):
        rel=f[len(root)+1:-len('/index.html')]; parts=rel.split('/'); slug=parts[-1]
        s=open(f).read()
        if 'www.viator.com' not in s: continue
        def rep(m):
            global n
            q=parse_qs(urlparse(html.unescape(m[1])).query); text=q['text'][0]; camp=q['campaign'][0]
            dest=S.get(slug)
            if dest is None:
                if parts[0]=='paris': dest='Paris'
                elif slug in ('que-faire-a-paris-en-hiver','things-to-do-in-paris-in-winter'): dest='Paris'
                elif slug in ('ou-partir-en-hiver','where-to-go-in-winter'): dest='Paris' if 'Paris' in text else 'Chamonix'
                else: miss.add((lang,rel,text)); return m[0]
            n+=1
            pre='https://www.viator.com/fr-FR/' if lang=='fr' else 'https://www.viator.com/'
            return f'href="{pre}{dest}/d{D[dest]}-ttd?pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign={camp}"'
        t=re.sub(r'href="(https://www\.viator\.com/[^"]*searchResults[^"]*)"',rep,s)
        if t!=s: open(f,'w').write(t)
print(n,'liens Viator remplacés; non mappés:',miss)
