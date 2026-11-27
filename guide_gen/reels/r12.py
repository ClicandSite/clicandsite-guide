import sys; sys.path.insert(0,'/tmp/reel'); from reel import render
N=' '
P=[
 dict(photo='noel-a-paris',credit='Pierre Blaché / Unsplash',kicker='PARIS · 25 DÉC. ET 1ER JANV.',title='Qu’est-ce qui est\nouvert à Paris ?',sub='Noël et le Jour de l’An tombent tous les deux un vendredi.'),
 dict(photo='tour-eiffel',credit='Anthony DELANOIX / Unsplash',kicker='OUVERT LES DEUX JOURS',title='La tour Eiffel',sub=f'Dès 9{N}h{N}30. Le 31 décembre, fermeture à 21{N}h.',out=1),
 dict(photo='notre-dame',credit='Maxime Gilbert / Unsplash',kicker='OUVERT LES DEUX JOURS',title='Notre-Dame et\nle Sacré-Cœur',sub='Entrée gratuite, tous les jours.'),
 dict(photo='musee-d-orsay',credit='Yomex Owo / Unsplash',kicker='OUVERT LE 1ER JANVIER',title='Le musée d’Orsay',sub='Fermé le 25. L’Orangerie et la Conciergerie aussi sont ouvertes le 1er janvier.',out=1),
 dict(photo='louvre',credit='Hongbin / Unsplash',kicker='FERMÉ LES DEUX JOURS',title='Le Louvre\net Versailles',sub='Comme l’Arc de Triomphe, les Invalides et les Catacombes.'),
 dict(photo='montmartre',credit='Maryline Waldy / Unsplash',kicker='LE GUIDE COMPLET',title='La liste complète\net nos idées',sub='Lien en bio · clicandsite.fr',end=1,out=1),
]
C=[
 dict(photo='carnaval-nice',credit='Pierre Goiffon / Unsplash',kicker='NICE · 9-28 FÉV. 2027',title='Carnaval de Nice :\n« Vive l’Amour »',sub='Le plus grand événement d’hiver de la Côte d’Azur.'),
 dict(photo='promenade-des-anglais',credit='Antoine Gravier / Unsplash',kicker='LES BATAILLES DE FLEURS',title='Nouveau parcours\nen 2027',sub=f'Sur la promenade des Anglais : mer. 17 et 24, sam. 20 et 27 février, à 14{N}h{N}30.',out=1),
 dict(photo='place-massena',credit='Lum Lumi / Unsplash',kicker='LES CORSOS ILLUMINÉS',title='Les corsos\nplace Masséna',sub=f'De nuit, en musique et en lumières. Ouverture le samedi 13 février à 21{N}h.'),
 dict(photo='nice',credit='Constantin / Unsplash',kicker='NOUVEAUTÉ 2027',title='Places debout\ngratuites',sub='Pour les corsos et les batailles de fleurs, sur réservation.',out=1),
 dict(photo='vieux-nice',credit='Nick Page / Unsplash',kicker='ENTRE DEUX DÉFILÉS',title='Le Vieux Nice\net le cours Saleya',sub='À deux pas de la place Masséna.'),
 dict(photo='nice',focus=0.2,credit='Constantin / Unsplash',kicker='LE GUIDE COMPLET',title='Programme, accès\net billets',sub='Lien en bio · clicandsite.fr',end=1,out=1),
]
render(C,'/tmp/ig/out/12-carnaval-nice-2027-reel.mp4')
