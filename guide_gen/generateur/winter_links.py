import re
L=[('clicandsite-guide','idees/stations-de-ski-ouvertes','À lire aussi : le <a href="../prix-forfaits-ski-2026-2027/">comparatif des prix des forfaits de ski 2026-2027</a> et les <a href="../vacances-de-fevrier-2027/">dates des vacances de février 2027</a>.'),
('clicandsite-guide','idees/ou-partir-en-hiver','À lire aussi : les <a href="../marches-de-noel-alsace/">marchés de Noël en Alsace</a>, le <a href="../reveillon-nouvel-an/">réveillon du Nouvel An</a>, les <a href="../vacances-de-fevrier-2027/">vacances de février 2027</a> et le <a href="../prix-forfaits-ski-2026-2027/">prix des forfaits de ski</a>.'),
('clicandsite-guide','alsace/strasbourg','À lire aussi : notre <a href="../../idees/marches-de-noel-alsace/">itinéraire des marchés de Noël en Alsace</a>, avec les dates de Colmar, Riquewihr et Kaysersberg.'),
('clicandsite-guide','alsace/colmar','À lire aussi : notre <a href="../../idees/marches-de-noel-alsace/">itinéraire des marchés de Noël en Alsace</a>, avec Strasbourg et les navettes vers les villages.'),
('clicandsite-guide','paris/noel-a-paris','À lire aussi : <a href="../../idees/reveillon-nouvel-an/">où fêter le réveillon du Nouvel An</a>, avec le feu d’artifice des Champs-Élysées.'),
('clicandsite-guide','idees/cote-d-azur-en-hiver','À lire aussi : le <a href="../../cote-d-azur/rallye-monte-carlo/">Rallye Monte-Carlo 2027</a>, la <a href="../../cote-d-azur/route-du-mimosa/">Route du Mimosa</a> et les <a href="../vacances-de-fevrier-2027/">vacances de février 2027</a>.'),
('clicandsite-guide','cote-d-azur/monaco','En janvier, ne manquez pas le <a href="../rallye-monte-carlo/">Rallye Monte-Carlo 2027</a>, du 21 au 24 janvier.'),
('clicandsite-guide','cote-d-azur/mandelieu-la-napoule','En février, voir notre guide de la <a href="../route-du-mimosa/">Route du Mimosa et de la Fête du Mimosa 2027</a>.'),
('clicandsite-guide-en','ideas/ski-resort-opening-dates','Read next: our <a href="../ski-pass-prices-2026-2027/">2026-2027 ski pass price comparison</a> and the <a href="../february-school-holidays-2027/">February 2027 school holiday dates</a>.'),
('clicandsite-guide-en','ideas/where-to-go-in-winter','Read next: the <a href="../alsace-christmas-markets/">Alsace Christmas markets</a>, <a href="../new-years-eve-france/">New Year’s Eve</a>, the <a href="../february-school-holidays-2027/">February 2027 school holidays</a> and <a href="../ski-pass-prices-2026-2027/">ski pass prices</a>.'),
('clicandsite-guide-en','alsace/strasbourg','Read next: our <a href="../../ideas/alsace-christmas-markets/">Alsace Christmas markets itinerary</a>, with the dates for Colmar, Riquewihr and Kaysersberg.'),
('clicandsite-guide-en','alsace/colmar','Read next: our <a href="../../ideas/alsace-christmas-markets/">Alsace Christmas markets itinerary</a>, with Strasbourg and the shuttles to the villages.'),
('clicandsite-guide-en','paris/christmas-in-paris','Read next: <a href="../../ideas/new-years-eve-france/">where to spend New Year’s Eve</a>, with the Champs-Élysées fireworks.'),
('clicandsite-guide-en','ideas/french-riviera-in-winter','Read next: the <a href="../../french-riviera/monte-carlo-rally/">Monte-Carlo Rally 2027</a>, the <a href="../../french-riviera/mimosa-route/">Mimosa Route</a> and the <a href="../february-school-holidays-2027/">February 2027 school holidays</a>.'),
('clicandsite-guide-en','french-riviera/monaco','In January, do not miss the <a href="../monte-carlo-rally/">Monte-Carlo Rally 2027</a>, from 21 to 24 January.'),
('clicandsite-guide-en','french-riviera/mandelieu-la-napoule','In February, see our guide to the <a href="../mimosa-route/">Mimosa Route and the 2027 Mimosa Festival</a>.')]
for r,p,t in L:
    f=f'{r}/{p}/index.html'; s=open(f).read()
    href=re.findall(r'href="([^"]+)"',t)[0]
    if href in s: print('skip',p); continue
    m=re.search(r'<h2 id="infos-2026"',s) or re.search(r'<h2[^>]*>(Nos conseils|Our tips|Tips)',s) or re.search(r'\s*<section class="book"',s)
    s=s[:m.start()]+f'<p class="voir">{t}</p>\n'+s[m.start():]
    open(f,'w').write(s); print('ok',p)
