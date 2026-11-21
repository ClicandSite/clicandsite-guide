import re, json, html
R='/home/claude/'
NB=' '
def fr(s):  # espaces insécables FR avant : ; ? !
    return re.sub(r' ([:;?!])', NB+r'\1', s)
def add(path, anchor_h2, h2, items, maj, faq=None, subs=()):
    s=open(path).read()
    assert 'id="infos-2026"' not in s, path
    lis=''.join(f'<li><strong>{a}</strong> : {b}</li>' if path.find('-en/')<0 else f'<li><strong>{a}</strong>: {b}</li>' for a,b in items)
    block=f'<h2 id="infos-2026">{h2}</h2><ul>{lis}</ul><p class="maj">{maj}</p>'
    if '-en/' not in path: block=fr(block)
    assert anchor_h2 in s, (path, anchor_h2); s=s.replace(anchor_h2, block+anchor_h2, 1)
    for a,b in subs:
        assert a in s, (path,a); s=s.replace(a,b)
    if faq:
        q,a=faq
        if '-en/' not in path: q,a=fr(q),fr(a)
        s=s.replace('<div class="faq">', f'<div class="faq"><details><summary>{html.escape(q,quote=False)}</summary><p>{html.escape(a,quote=False)}</p></details>',1)
        def addld(m):
            j=json.loads(m.group(1))
            items=j if isinstance(j,list) else j.get('@graph',[j])
            for x in items:
                if isinstance(x,dict) and x.get('@type')=='FAQPage':
                    x['mainEntity'].insert(0,{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}})
            return '<script type="application/ld+json">'+json.dumps(j,ensure_ascii=False)+'</script>'
        s2=re.sub(r'<script type="application/ld\+json">(.*?)</script>',lambda m: addld(m) if 'FAQPage' in m.group(1) else m.group(0),s,flags=re.S)
        assert s2!=s; s=s2
    open(path,'w').write(s); print('ok',path)

MAJ_FR='Tarifs et dates relevés le 16 novembre 2026 auprès de la station, de l’office de tourisme et des grilles publiées pour 2026-2027 ; ils peuvent changer en cours de saison, vérifiez avant de partir.'
MAJ_EN='Prices and dates checked on 16 November 2026 with the resort, the tourist office and the published 2026-2027 price lists; they can change during the season, so check before you go.'

# ---------- Isola 2000
add(R+'clicandsite-guide/alpes/isola-2000/index.html','<h2>Nos conseils pour profiter d’Isola 2000</h2>','Infos pratiques 2026 : Isola 2000',[
 ('Saison','domaine ouvert du 3 décembre 2026 au 19 avril 2027, de 9 h à 17 h, sous réserve d’enneigement.'),
 ('Forfait journée','44 € pour un adulte (26-61 ans), 37 € pour les 12-25 ans et les 62-71 ans, 33,70 € pour les 5-11 ans ; 35,20 € l’après-midi adulte, à partir de 12 h 30.'),
 ('Forfait 6 jours','217 € pour un adulte en haute saison, 188,80 € en basse saison.'),
 ('Débutants','un forfait gratuit donne accès au téléski et au tapis du front de neige.')],MAJ_FR,
 faq=('Combien coûte le forfait à Isola 2000 en 2026-2027 ?','44 € la journée pour un adulte, 37 € pour les 12-25 ans et les 62-71 ans, 33,70 € pour les 5-11 ans. Le forfait débutant du front de neige est gratuit.'))
add(R+'clicandsite-guide-en/french-alps/isola-2000/index.html','<h2>Tips for a ski trip to Isola 2000</h2>','Practical info 2026: Isola 2000',[
 ('Season','the ski area is open from 3 December 2026 to 19 April 2027, 9am to 5pm, snow permitting.'),
 ('Day pass','€44 for an adult (26-61), €37 for ages 12-25 and 62-71, €33.70 for ages 5-11; €35.20 for an adult afternoon pass, from 12.30pm.'),
 ('6-day pass','€217 for an adult in high season, €188.80 in low season.'),
 ('Beginners','a free pass covers the drag lift and the conveyor on the front de neige.')],MAJ_EN,
 faq=('How much is a lift pass at Isola 2000 in 2026-2027?','€44 a day for an adult, €37 for ages 12-25 and 62-71, €33.70 for ages 5-11. The beginner pass for the front de neige is free.'))

# ---------- Auron
add(R+'clicandsite-guide/alpes/auron/index.html','<h2>Nos conseils pour profiter d’Auron</h2>','Infos pratiques 2026 : Auron',[
 ('Ouverture','prévue le 5 décembre 2026, sous réserve d’enneigement, sur 135 km de pistes.'),
 ('Forfait journée','44 € pour un adulte, 37 € pour les 12-25 ans et les 62-71 ans, 33,70 € pour les 5-11 ans.'),
 ('Forfait saison','689 € pour un adulte (26-61 ans) s’il est acheté jusqu’au 22 novembre 2026 inclus, aux caisses de la place centrale, ouvertes tous les jours de 10 h à 12 h et de 14 h à 16 h.'),
 ('Forfait 6 jours','217 € pour un adulte en haute saison.')],MAJ_FR,
 faq=('Combien coûte le forfait à Auron en 2026-2027 ?','44 € la journée pour un adulte, 37 € pour les 12-25 ans et les 62-71 ans, 33,70 € pour les 5-11 ans. Le forfait saison adulte coûte 689 € s’il est acheté avant le 23 novembre 2026.'))
add(R+'clicandsite-guide-en/french-alps/auron/index.html','<h2>Tips for a ski trip to Auron</h2>','Practical info 2026: Auron',[
 ('Opening','planned for 5 December 2026, snow permitting, across 135 km of runs.'),
 ('Day pass','€44 for an adult, €37 for ages 12-25 and 62-71, €33.70 for ages 5-11.'),
 ('Season pass','€689 for an adult (26-61) if bought by 22 November 2026, at the ticket offices on the main square, open daily from 10am to 12pm and 2pm to 4pm.'),
 ('6-day pass','€217 for an adult in high season.')],MAJ_EN,
 faq=('How much is a lift pass in Auron in 2026-2027?','€44 a day for an adult, €37 for ages 12-25 and 62-71, €33.70 for ages 5-11. The adult season pass costs €689 if bought before 23 November 2026.'))

# ---------- Font-Romeu
add(R+'clicandsite-guide/pyrenees/font-romeu/index.html','<h2>Nos conseils pour profiter de Font-Romeu</h2>','Infos pratiques 2026 : Font-Romeu',[
 ('Saison','domaine de Font-Romeu Pyrénées 2000 ouvert du 4 décembre 2026 au 29 mars 2027.'),
 ('Forfait journée','49,50 € pour un adulte, 42,50 € en tarif réduit ; 46 € pour 4 heures.'),
 ('Forfait 6 jours','256 € pour un adulte, 217 € en tarif réduit.'),
 ('Forfait saison','650 € pour un adulte, 492 € en tarif réduit.')],MAJ_FR,
 faq=('Combien coûte le forfait à Font-Romeu en 2026-2027 ?','49,50 € la journée pour un adulte, 42,50 € en tarif réduit, et 256 € les 6 jours pour un adulte.'),
 subs=[('jusqu’à la fin mars ou au début avril 2027 selon l’enneigement','jusqu’au 29 mars 2027, selon l’enneigement')])
add(R+'clicandsite-guide-en/pyrenees/font-romeu/index.html','<h2>Tips for a ski trip to Font-Romeu</h2>','Practical info 2026: Font-Romeu',[
 ('Season','the Font-Romeu Pyrénées 2000 ski area is open from 4 December 2026 to 29 March 2027.'),
 ('Day pass','€49.50 for an adult, €42.50 at the reduced rate; €46 for 4 hours.'),
 ('6-day pass','€256 for an adult, €217 at the reduced rate.'),
 ('Season pass','€650 for an adult, €492 at the reduced rate.')],MAJ_EN,
 faq=('How much is a lift pass in Font-Romeu in 2026-2027?','€49.50 a day for an adult, €42.50 at the reduced rate, and €256 for 6 days for an adult.'),
 subs=[('until late March or early April 2027 depending on snow','until 29 March 2027, depending on snow'),('<dd>Late March or early April 2027</dd>','<dd>29 March 2027</dd>')])

# ---------- Chamonix
add(R+'clicandsite-guide/alpes/chamonix/index.html','<h2>Nos conseils pour profiter de Chamonix</h2>','Infos pratiques 2026 : Chamonix',[
 ('Chamonix Le Pass','76,50 € la journée adulte du 19 décembre 2026 au 9 avril 2027, 61,20 € en début et en fin de saison, et dès 49 € en achat anticipé en ligne.'),
 ('Le Pass 6 jours','373 € pour un adulte en haute saison, 290,40 € au tarif de printemps à partir du 10 avril 2027.'),
 ('Mont-Blanc Unlimited','104 € la journée adulte : il ajoute Les Houches, l’Aiguille du Midi, le Montenvers et les domaines voisins de la vallée.'),
 ('Ouverture','les premiers secteurs, les Grands Montets et la Flégère, ouvrent fin novembre, le reste de la vallée en décembre.')],
 'Tarifs relevés le 16 novembre 2026 sur les grilles 2026-2027 publiées ; les prix en ligne varient selon la date, vérifiez avant de partir.',
 faq=('Combien coûte le forfait à Chamonix en 2026-2027 ?','Chamonix Le Pass coûte 76,50 € la journée adulte en haute saison, 61,20 € en début et en fin de saison, et dès 49 € en ligne. Le Mont-Blanc Unlimited coûte 104 € la journée.'))
add(R+'clicandsite-guide-en/french-alps/chamonix/index.html','<h2>Tips for a winter trip to Chamonix</h2>','Practical info 2026: Chamonix',[
 ('Chamonix Le Pass','€76.50 a day for an adult from 19 December 2026 to 9 April 2027, €61.20 early and late in the season, and from €49 when bought online in advance.'),
 ('Le Pass, 6 days','€373 for an adult in high season, €290.40 at the spring rate from 10 April 2027.'),
 ('Mont-Blanc Unlimited','€104 a day for an adult: it adds Les Houches, the Aiguille du Midi, the Montenvers and the valley’s neighbouring ski areas.'),
 ('Opening','the first areas, Grands Montets and La Flégère, open in late November, the rest of the valley in December.')],
 'Prices checked on 16 November 2026 from the published 2026-2027 price lists; online prices vary by date, so check before you go.',
 faq=('How much is a lift pass in Chamonix in 2026-2027?','Chamonix Le Pass costs €76.50 a day for an adult in high season, €61.20 early and late in the season, and from €49 online. The Mont-Blanc Unlimited costs €104 a day.'))
