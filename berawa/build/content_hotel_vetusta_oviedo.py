# Contenido de la demo Hotel Vetusta (Oviedo) (es/en/fr/de). Hechos de hotelvetusta.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios de habitacion ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Habitación individual','Habitación económica','Habitación matrimonial','Doble o twin + cama extra'],
'en':['Single room','Economy room','Double room','Double or twin + extra bed'],
'fr':['Chambre individuelle','Chambre économique','Chambre double','Double ou twin + lit supplémentaire'],
'de':['Einzelzimmer','Economy-Zimmer','Doppelzimmer','Doppel- oder Zweibettzimmer + Zustellbett']}
RD={
'es':['Para una persona: puedes elegir la almohada. Wi-Fi gratuito, aire acondicionado, TV LCD, caja de seguridad y amenities.','Preparada para dos huéspedes, con Wi-Fi, aire acondicionado, TV LCD y amenities.','Para dos huéspedes y con balcón. Wi-Fi, aire acondicionado, TV LCD y amenities.','Capacidad máxima para tres personas, pensada para familias o amigos. Wi-Fi, aire acondicionado, TV LCD y amenities.'],
'en':['For one guest: you can choose your pillow. Free Wi-Fi, air conditioning, LCD TV, safe and toiletries.','Ready for two guests, with Wi-Fi, air conditioning, LCD TV and toiletries.','For two guests, with a balcony. Wi-Fi, air conditioning, LCD TV and toiletries.','Up to three people, ideal for families or friends. Wi-Fi, air conditioning, LCD TV and toiletries.'],
'fr':['Pour une personne : vous pouvez choisir votre oreiller. Wi-Fi gratuit, climatisation, TV LCD, coffre-fort et produits d\'accueil.','Prévue pour deux personnes, avec Wi-Fi, climatisation, TV LCD et produits d\'accueil.','Pour deux personnes, avec balcon. Wi-Fi, climatisation, TV LCD et produits d\'accueil.','Jusqu\'à trois personnes, idéale pour les familles ou les amis. Wi-Fi, climatisation, TV LCD et produits d\'accueil.'],
'de':['Für eine Person: Sie können Ihr Kopfkissen wählen. Kostenloses WLAN, Klimaanlage, LCD-TV, Safe und Pflegeartikel.','Für zwei Gäste eingerichtet, mit WLAN, Klimaanlage, LCD-TV und Pflegeartikeln.','Für zwei Gäste, mit Balkon. WLAN, Klimaanlage, LCD-TV und Pflegeartikel.','Für bis zu drei Personen, ideal für Familien oder Freunde. WLAN, Klimaanlage, LCD-TV und Pflegeartikel.']}
ART={
'hero':('skyline',9101,['#24435a','#e3b27a','#f4dcb4','#2f5a73','#1f3d51','#132a39']),
'intro':('columns',9102,['#ecebe6','#f8f6f1','#9a6b2f','#24435a','#16293a']),
'r1':('arches',9111,['#efe6d6','#dfb07c','#a0602c','#24435a','#16293a']),
'r2':('hills',9112,['#e4ebe6','#efe7d2','#e6b677','#9fb7a6','#6f8f80','#46695d']),
'r3':('columns',9113,['#ebe8e1','#f7f4ee','#a5652f','#24435a','#16293a']),
'r4':('waves',9114,['#24435a','#ebba80','#f6deb5','#356580','#24435a','#16293a']),
'g1':('skyline',9121,['#2f5a73','#e0a868','#f3d6a6','#24435a','#1b3446','#112333']),
'g2':('hills',9122,['#e3eae2','#eee6ce','#eab875','#a4ba9a','#78977e','#4f7059']),
'g3':('arches',9123,['#ece3d2','#dcab76','#9e5a26','#24435a','#16293a']),
'g4':('waves',9124,['#24435a','#edbd83','#f6deb5','#3c6a86','#24435a','#16293a'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3','r4'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Vetusta · Hotel de 3 estrellas en el centro de Oviedo',see_rooms='Ver las habitaciones',hero_k='Oviedo · Asturias',hero_t='Cálido y acogedor, en el centro de Oviedo',hero_s='Hotel de 3 estrellas a tan solo 2 minutos del casco antiguo y la zona comercial.',
 intro_t='Tu hotel en el centro de Oviedo',intro_p1='Habitaciones amplias con los servicios esenciales para una estancia cómoda, atención personalizada y cafetería propia con repostería casera.',
 intro_p2='Recepción de 7:00 a 22:30 de lunes a viernes y de 8:00 a 22:30 sábados y domingos, con información turística para preparar tu visita.',
 stats=['3 estrellas','Wi-Fi gratuito','Cafetería y terraza','Servicio de habitaciones'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Cuatro tipos de habitación, de una a tres personas.',
 svcs=['Wi-Fi gratuito en todo el hotel','Aire acondicionado','Bar-cafetería','Servicio de habitaciones sin coste adicional','Acuerdo con el Parking Longoria','Información turística'],
 around_s='A 2 minutos del casco antiguo. Su web recomienda el Mercado de El Fontán y el monte Naranco.',
 loc_p='C. Covadonga, 2 · 33002 Oviedo (Asturias), a 2 minutos del casco antiguo y la zona comercial.',
 chips=['¿Qué habitaciones tenéis?','¿A qué hora es el check-in?','¿Dónde aparco?','¿Admitís mascotas?']),
'en':dict(title='Hotel Vetusta · 3-star hotel in the centre of Oviedo',see_rooms='See the rooms',hero_k='Oviedo · Asturias',hero_t='Warm and cosy, in the centre of Oviedo',hero_s='3-star hotel just 2 minutes from the old town and the shopping area.',
 intro_t='Your hotel in the centre of Oviedo',intro_p1='Spacious rooms with all the essentials for a comfortable stay, personal attention and its own cafeteria with homemade pastries.',
 intro_p2='Reception is open from 7:00 to 22:30 Monday to Friday and from 8:00 to 22:30 on Saturdays and Sundays, with tourist information to plan your visit.',
 stats=['3 stars','Free Wi-Fi','Cafeteria and terrace','Room service'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Four room types, for one to three people.',
 svcs=['Free Wi-Fi throughout the hotel','Air conditioning','Bar-cafeteria','Room service at no extra cost','Agreement with Parking Longoria','Tourist information'],
 around_s='2 minutes from the old town. Their website recommends the El Fontán market and Mount Naranco.',
 loc_p='C. Covadonga, 2 · 33002 Oviedo (Asturias), 2 minutes from the old town and the shopping area.',
 chips=['Which rooms do you have?','What time is check-in?','Where can I park?','Are pets allowed?']),
'fr':dict(title='Hotel Vetusta · Hôtel 3 étoiles au centre d\'Oviedo',see_rooms='Voir les chambres',hero_k='Oviedo · Asturies',hero_t='Chaleureux et accueillant, au centre d\'Oviedo',hero_s='Hôtel 3 étoiles à seulement 2 minutes de la vieille ville et du quartier commerçant.',
 intro_t='Votre hôtel au centre d\'Oviedo',intro_p1='Des chambres spacieuses avec l\'essentiel pour un séjour confortable, un accueil personnalisé et une cafétéria avec pâtisserie maison.',
 intro_p2='Réception ouverte de 7h00 à 22h30 du lundi au vendredi et de 8h00 à 22h30 le samedi et le dimanche, avec des informations touristiques pour préparer votre visite.',
 stats=['3 étoiles','Wi-Fi gratuit','Cafétéria et terrasse','Service en chambre'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Quatre types de chambre, pour une à trois personnes.',
 svcs=['Wi-Fi gratuit dans tout l\'hôtel','Climatisation','Bar-cafétéria','Service en chambre sans frais supplémentaires','Accord avec le Parking Longoria','Informations touristiques'],
 around_s='À 2 minutes de la vieille ville. Leur site recommande le marché d\'El Fontán et le mont Naranco.',
 loc_p='C. Covadonga, 2 · 33002 Oviedo (Asturies), à 2 minutes de la vieille ville et du quartier commerçant.',
 chips=['Quelles chambres avez-vous ?','À quelle heure est le check-in ?','Où me garer ?','Les animaux sont-ils admis ?']),
'de':dict(title='Hotel Vetusta · 3-Sterne-Hotel im Zentrum von Oviedo',see_rooms='Zimmer ansehen',hero_k='Oviedo · Asturien',hero_t='Herzlich und gemütlich, im Zentrum von Oviedo',hero_s='3-Sterne-Hotel nur 2 Minuten von der Altstadt und dem Einkaufsviertel entfernt.',
 intro_t='Ihr Hotel im Zentrum von Oviedo',intro_p1='Geräumige Zimmer mit allem Wesentlichen für einen angenehmen Aufenthalt, persönlicher Service und eine eigene Cafeteria mit hausgemachtem Gebäck.',
 intro_p2='Die Rezeption ist montags bis freitags von 7:00 bis 22:30 Uhr und samstags und sonntags von 8:00 bis 22:30 Uhr geöffnet und hilft Ihnen mit touristischen Informationen.',
 stats=['3 Sterne','Kostenloses WLAN','Cafeteria und Terrasse','Zimmerservice'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Vier Zimmertypen für eine bis drei Personen.',
 svcs=['Kostenloses WLAN im ganzen Hotel','Klimaanlage','Bar-Cafeteria','Zimmerservice ohne Aufpreis','Vereinbarung mit dem Parking Longoria','Touristische Informationen'],
 around_s='2 Minuten von der Altstadt. Die Website empfiehlt den Markt El Fontán und den Berg Naranco.',
 loc_p='C. Covadonga, 2 · 33002 Oviedo (Asturien), 2 Minuten von der Altstadt und dem Einkaufsviertel entfernt.',
 chips=['Welche Zimmer gibt es?','Wann ist der Check-in?','Wo kann ich parken?','Sind Haustiere erlaubt?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RES='https://www.hotelvetusta.com/reservar.html'; RES_EN='https://www.hotelvetusta.com/EN/booking.html'
BOOK=dict(mode='engine',url={'es':RES,'en':RES_EN,'fr':RES_EN,'de':RES_EN})
D=dict(name='Hotel Vetusta',ac='#24435a',ac2='#9a6b2f',ac2_a11y='#6d4a17',book=BOOK,around=['Mercado de El Fontán','Monte Naranco'],foot=FOOT,
 address='C. Covadonga, 2 · 33002 Oviedo (Asturias)',phones=['+34 985 22 22 29'],emails=['info@hotelvetusta.com'],maps='Hotel Vetusta, Calle Covadonga 2, Oviedo',t=T)
META=dict(repo='demo-hotel-vetusta-oviedo',name='Hotel Vetusta',legal_name='Alojamiento Hotelero Vetusta',registry_ids=['CIF B74308990'],
 url='https://www.hotelvetusta.com/',domain='hotelvetusta.com',municipality='Oviedo',province='Asturias',sector='hotel urbano de 3 estrellas en el centro de Oviedo',
 read_at='2026-10-30T06:47:00+01:00',created_at='2026-10-30T06:46:00+01:00',built_at='2026-10-30T07:05:00+01:00',audit_date='2026-10-30T06:43:00+01:00',
 rating=dict(value=4.1,coincide=['telefono','web'],date='2026-10-29T12:23:47+01:00',url='https://www.google.com/maps/place/Hotel+Vetusta/@43.3640247,-5.8471744,17z/data=!4m9!3m8!1s0xd368cfab7624ea5:0xf26c936619f7c09!5m2!4m1!1i2!8m2!3d43.3640247!4d-5.8471744!16s%2Fg%2F1tgz1wmk'),
 book=dict(mode='engine',url=RES,note='motor de reservas propio de su web (reservar.html, Keytel), HTTP 200 comprobado el 30/10/2026.'),first_of_type=None)
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Tenéis habitación para tres personas?','K02'),('¿Hay wifi?','K03'),('¿A qué hora es el check-in?','K04'),('¿Dónde aparco?','K05'),('¿Admitís mascotas?','K06'),('¿Hay cafetería?','K07'),('¿Dónde está el hotel?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Cuánto cuesta una noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Do you have a room for three people?','K02'),('Is there wifi?','K03'),('What time is check-in?','K04'),('Where can I park?','K05'),('Are pets allowed?','K06'),('Is there a cafeteria?','K07'),('Where is the hotel?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Avez-vous une chambre pour trois personnes ?','K02'),('Y a-t-il le wifi ?','K03'),('À quelle heure est le check-in ?','K04'),('Où me garer ?','K05'),('Les animaux sont-ils admis ?','K06'),('Y a-t-il une cafétéria ?','K07'),('Où se trouve l\'hôtel ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Combien coûte une nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Haben Sie ein Zimmer für drei Personen?','K02'),('Gibt es WLAN?','K03'),('Wann ist der Check-in?','K04'),('Wo kann ich parken?','K05'),('Sind Haustiere erlaubt?','K06'),('Gibt es eine Cafeteria?','K07'),('Wo liegt das Hotel?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Was kostet eine Übernachtung?',None),('Haben Sie ein Schwimmbad?',None)]}
