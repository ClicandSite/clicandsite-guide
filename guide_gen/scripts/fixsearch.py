import re,glob,json,html
from urllib.parse import unquote_plus
M={
"Antibes":"antibes-l5075/","Antibes Biot":"antibes-l5075/","Antibes French Riviera hilltop villages":"saint-paul-de-vence-l91755/",
"Cannes":"cannes-l15/","Cannes Lerins Islands":"lerins-islands-l9834/","Cannes boat":"cannes-l15/cruises-boat-tours-tc48/",
"Cap d'Antibes boat":"antibes-l5075/cruises-boat-tours-tc48/","Chamonix Aiguille du Midi":"aiguille-du-midi-l117540/",
"Colmar Christmas markets tour":"colmar-l2924/christmas-market-tours-tc2182/","Colmar Little Venice boat":"colmar-l2924/",
"Disneyland Paris ticket":"disneyland-paris-l2603/","Disneyland Paris transfer":"disneyland-paris-l2603/",
"Eze Monaco":"eze-l12561/","Eze perfume":"eze-l12561/",
"French Alps ski":"haute-savoie-l120865/snow-winter-sports-tc113/","French Alps ski lessons":"auvergne-rhone-alpes-l132103/snow-winter-sports-tc113/",
"French Riviera day trip Nice Monaco":"nice-l314/day-trips-tc172/","Gourdon Grasse tour":"grasse-l2037/","Grasse Gorges du Loup":"grasse-l2037/",
"Grasse day trip":"grasse-l2037/","Grasse perfume workshop":"grasse-l2037/","Hyeres islands boat":"ile-de-porquerolles-l39692/",
"Hyères Porquerolles":"ile-de-porquerolles-l39692/","Menton":"menton-l294/","Menton Italy day trip":"menton-l294/day-trips-tc172/",
"Menton Roquebrune-Cap-Martin":"menton-l294/","Monaco":"monaco-l515/","Monaco Eze day trip":"monaco-l515/","Monaco Menton day trip":"menton-l294/",
"Mougins":"mougins-l102402/","Mougins Grasse tour":"grasse-l2037/","Moustiers-Sainte-Marie Verdon Gorge":"verdon-gorge-l96055/",
"Moustiers-Sainte-Marie Verdon canoe rafting":"verdon-gorge-l96055/","Nice carnival":"nice-l314/","Nice day trip":"nice-l314/day-trips-tc172/",
"Nice walking tour":"nice-l314/walking-tours-tc3/","Palace of Versailles":"palace-of-versailles-l317/","Pantheon Paris":"pantheon-paris-l4381/",
"Paris Arc de Triomphe":"arc-de-triomphe-l3238/","Paris Arc de Triomphe ticket":"arc-de-triomphe-l3238/entry-tickets-tc123/",
"Paris Catacombs":"paris-catacombs-l2605/","Paris Champs-Elysees tour":"champs-elysees-l3452/","Paris Christmas cruise":"seine-river-l2601/",
"Paris Christmas lights tour":"paris-l16/","Paris Eiffel Tower":"eiffel-tower-l2600/","Paris Eiffel Tower Seine cruise":"seine-river-l2601/",
"Paris Latin Quarter guided tour":"latin-quarter-l3260/","Paris Latin Quarter walking tour":"latin-quarter-l3260/",
"Paris Louvre Museum ticket":"louvre-museum-l3224/entry-tickets-tc123/","Paris Louvre guided tour":"louvre-museum-l3224/guided-tours-tc1144/",
"Paris Marais food tour":"le-marais-l3226/local-food-tours-tc532/","Paris Marais walking tour":"le-marais-l3226/",
"Paris Montmartre food tour":"montmartre-l2607/local-food-tours-tc532/","Paris Montmartre walking tour":"montmartre-l2607/",
"Paris Moulin Rouge dinner show":"moulin-rouge-l2604/","Paris Moulin Rouge show":"moulin-rouge-l2604/","Paris Musee d'Orsay":"musee-d-orsay-l2976/",
"Paris Notre-Dame Sainte-Chapelle":"sainte-chapelle-l3229/","Paris Notre-Dame guided tour":"notre-dame-cathedral-l3230/",
"Paris Orangerie museum ticket":"musee-de-l-orangerie-l3222/","Paris Orsay Orangerie":"musee-de-l-orangerie-l3222/",
"Paris Orsay Orangerie combo ticket":"musee-d-orsay-l2976/","Paris Palais Garnier":"palais-garnier-l3218/","Paris Palais Garnier guided tour":"palais-garnier-l3218/",
"Paris Pantheon ticket":"pantheon-paris-l4381/","Paris Sainte-Chapelle concert":"sainte-chapelle-l3229/","Paris Sainte-Chapelle ticket":"sainte-chapelle-l3229/",
"Paris Seine dinner cruise":"seine-river-l2601/","Paris museum tickets":"paris-l16/","Paris underground tour":"paris-catacombs-l2605/",
"Saint-Jean-Cap-Ferrat Cap Ferrat boat":"villefranche-sur-mer-l1706/","Saint-Jean-Cap-Ferrat Villa Ephrussi Rothschild":"villa-ephrussi-de-rothschild-l136993/",
"Saint-Paul-de-Vence":"saint-paul-de-vence-l91755/","Saint-Paul-de-Vence Grasse hilltop villages":"saint-paul-de-vence-l91755/",
"Saint-Raphaël Esterel":"frejus-saint-raphael-l32405/","Saint-Raphaël Esterel boat":"frejus-saint-raphael-l32405/cruises-boat-tours-tc48/",
"Saint-Tropez":"saint-tropez-l518/","Saint-Tropez boat":"saint-tropez-l518/cruises-boat-tours-tc48/","Seine river cruise Paris":"seine-river-l2601/",
"Strasbourg Christmas market tour":"strasbourg-l293/christmas-market-tours-tc2182/","Strasbourg boat cruise":"strasbourg-l293/",
"Versailles bike tour":"palace-of-versailles-l317/","Villefranche-sur-Mer":"villefranche-sur-mer-l1706/","Villefranche-sur-Mer Villefranche Eze Monaco":"villefranche-sur-mer-l1706/",
}
pairs=json.load(open('/tmp/qpairs.json'))
FR={f:e for e,fs in pairs.items() for f in fs}
if __name__=='__main__':
    import sys
    if sys.argv[1:]==['paths']:
        print(json.dumps(sorted(set(M.values())))); sys.exit()
    n=0; miss=set()
    for root,host,lang in (('/home/claude/clicandsite-guide','fr','fr'),('/home/claude/clicandsite-guide-en','com','en')):
        for f in glob.glob(root+'/**/*.html',recursive=True):
            s=open(f).read()
            def rep(m):
                global n
                q=unquote_plus(html.unescape(m[1])); e=q if lang=='en' else FR.get(q)
                if e not in M: miss.add((lang,q)); return m[0]
                n+=1; return f'https://www.getyourguide.{host}/{M[e]}?partner_id'
            t=re.sub(r'https://www\.getyourguide\.(?:fr|com)/s/\?q=([^&"]*)&amp;partner_id',rep,s)
            if t!=s: open(f,'w').write(t)
    print(n,miss)
