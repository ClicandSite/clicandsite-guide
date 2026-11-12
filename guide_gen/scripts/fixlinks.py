import re,os
from urllib.parse import quote_plus
ARA_SNOW='auvergne-rhone-alpes-l132103/snow-winter-sports-tc113/'
ARA_WIN='auvergne-rhone-alpes-l132103/winter-activities-tc2023/'
HS_SNOW='haute-savoie-l120865/snow-winter-sports-tc113/'
M={ # slug: ([gyg act1, act2], viator text fr, viator text en)
 'chamonix':(['chamonix-mont-blanc-l1773/','chamonix-mont-blanc-l1773/'],'Chamonix','Chamonix'),
 'megeve':(['megeve-l2942/','chamonix-mont-blanc-l1773/'],'Megève','Megeve'),
 'courchevel':(['courchevel-l201172/',ARA_SNOW],'Courchevel','Courchevel'),
 'meribel':([ARA_SNOW,'courchevel-l201172/'],'Alpes françaises','French Alps'),
 'val-thorens':([ARA_SNOW,ARA_WIN],'Alpes françaises','French Alps'),
 'les-menuires':([ARA_SNOW,ARA_WIN],'Alpes françaises','French Alps'),
 'val-d-isere':([ARA_SNOW,ARA_WIN],'Alpes françaises','French Alps'),
 'tignes':([ARA_SNOW,ARA_WIN],'Alpes françaises','French Alps'),
 'les-arcs':([ARA_SNOW,ARA_WIN],'Alpes françaises','French Alps'),
 'la-plagne':([ARA_SNOW,'la-plagne-l87621/'],'Alpes françaises','French Alps'),
 'avoriaz':(['morzine-l207775/',HS_SNOW],'Morzine','Morzine'),
 'chatel':(['morzine-l207775/',HS_SNOW],'Morzine','Morzine'),
 'la-clusaz':([HS_SNOW,'haute-savoie-l120865/'],'Annecy','Annecy'),
 'les-2-alpes':(['grenoble-l98511/',ARA_SNOW],'Grenoble','Grenoble'),
 'alpe-d-huez':(['grenoble-l98511/',ARA_SNOW],'Grenoble','Grenoble'),
 'serre-chevalier':(['briancon-l227363/',ARA_SNOW],'Briançon','Briancon'),
 'kaysersberg':(['colmar-l2924/christmas-market-tours-tc2182/','colmar-l2924/'],'Colmar','Colmar'),
 'riquewihr':(['colmar-l2924/christmas-market-tours-tc2182/','colmar-l2924/'],'Colmar','Colmar'),
}
for root,lang,regs in (('/home/claude/clicandsite-guide','fr',{'alpes':'alpes','alsace':'alsace'}),('/home/claude/clicandsite-guide-en','en',{'alpes':'french-alps','alsace':'alsace'})):
    for slug,(g,vfr,ven) in M.items():
        reg='alsace' if slug in('kaysersberg','riquewihr') else 'alpes'
        f=f"{root}/{regs[reg]}/{slug}/index.html"
        if not os.path.exists(f): print('missing',f); continue
        s=open(f).read(); tag=f"{regs[reg]}-{slug}"
        host='https://www.getyourguide.fr/' if lang=='fr' else 'https://www.getyourguide.com/'
        vt=vfr if lang=='fr' else ven
        vhost='https://www.viator.com/fr-FR/searchResults/all' if lang=='fr' else 'https://www.viator.com/searchResults/all'
        i=[0]
        def rg(m):
            k=min(i[0],len(g)-1); i[0]+=1
            return f'class="bk bk--gyg" href="{host}{g[k]}?partner_id=XMYSXGR&amp;cmp=clicandsite-{lang}-{tag}&amp;utm_medium=online_publisher"'
        s2=re.sub(r'class="bk bk--gyg" href="https://www\.getyourguide[^"]*"',rg,s)
        s2=re.sub(r'class="bk bk--via" href="https://www\.viator[^"]*"',lambda m:f'class="bk bk--via" href="{vhost}?text={quote_plus(vt)}&amp;pid=P00331213&amp;mcid=42383&amp;medium=link&amp;campaign=clicandsite-{lang}-{tag}"',s2)
        if s2!=s: open(f,'w').write(s2)
        print(lang,slug,i[0])
