"""Arma GOLD-STUDIO-25-OCT-AL-7-NOV.zip (carpetas por día con archivo + texto) e historias-semana-19-al-25.zip."""
import zipfile, glob, os
F = '/home/user/gold-studio-final/'
R, C = F + 'reels/', F + 'carruseles/'
POSTS = [
 ('Dom 25-10', '18h30', 'Reel', 'Un día en Gold Studio', R + 'dia18-reel-un-dia-en-gold-studio.mp4',
  'Un día cualquiera en Gold Studio, sin mostrar mi cara ✦\nCafé, música tranqui y una marca nueva para armar.\n\n¿Vos cómo arrancás tus días de trabajo?\n\n#emprendedorasargentinas #diseñografico #detrasdeescena',
  None),
 ('Lun 26-10', '10h00', 'Reel', 'Le cambié la cara a una marca', R + 'dia19-reel-prana-antes-despues.mp4',
  'Le cambié la cara a una marca en 30 segundos ✦\nDe un logo genérico a una identidad que transmite calma: colores, tipografía, logo y aplicaciones.\n\n(Prana es una marca de ejemplo.)\n\n¿Cuál fue tu parte favorita?\n\n#branding #identidaddemarca #diseñodelogos', None),
 ('Mar 27-10', '18h00', 'Carrusel', 'El packaging también vende', C + 'carrusel-packaging',
  'El packaging es lo primero que tu clienta toca de tu marca ✦\nCaja, sticker, tarjeta y bolsa: cuando todo combina, se nota.\n\nGuardalo para cuando armes el tuyo.\n\n#packaging #branding #emprendedorasargentinas', None),
 ('Mie 28-10', '10h00', 'Reel', 'Así se ve mi página por dentro', R + 'dia21-reel-mi-web-por-dentro.mp4',
  'Así se ve mi página web por dentro ✦\nQué hago, mis servicios, un trabajo real que podés probar, los paquetes y un botón para escribirme.\n\nEl link está en mi bio.\n\n#paginaweb #diseñoweb #emprendedorasargentinas', None),
 ('Jue 29-10', '18h00', 'Carrusel', 'Tener un logo no es tener una marca', C + 'carrusel-logos-e-identidad',
  'Tener un logo no es tener una marca ✦\nLos 5 tipos de logo y todo lo que los convierte en identidad.\n\n¿Cuál tiene tu marca? Contame abajo.\n\n#branding #identidaddemarca #logo', None),
 ('Vie 30-10', '10h00', 'Reel', 'Cosas que dan miedo en una marca', R + 'dia24-reel-halloween-marcas-que-dan-miedo.mp4',
  'Especial Halloween: cosas que dan miedo en una marca 👻\nCinco tipografías, logo pixelado, perfil sin bio, link roto y un feed de mil colores.\n\n¿Cuántas tenía la tuya? Sin vergüenza, jaja.\n\n#halloween #branding #marketingdigital', None),
 ('Sab 31-10', '10h00', 'Carrusel', 'Antes y después de un feed', C + 'dia25-carrusel-antes-despues-feed',
  'Antes y después de un feed ✦\nFoto de perfil, bio, destacadas y grilla: cuatro cambios y el perfil parece otra marca.\n\n(Brisa es una marca de ejemplo.)\nGuardalo y revisá el tuyo.\n\n#instagramtips #communitymanager #emprendedorasargentinas', None),
 ('Dom 01-11', '18h30', 'Reel', 'Cómo elegir el nombre de tu marca', R + 'dia25-reel-como-elegir-el-nombre.mp4',
  'Cómo elegir el nombre de tu marca ✦\nEscribí muchas opciones, que sea corto, que esté libre, imaginalo como logo y preguntá a 3 personas.\n\n(Miga es una marca de ejemplo.)\n¿Cómo elegiste el nombre de la tuya?\n\n#emprendimiento #branding #emprendedorasargentinas',
  None),
 ('Lun 02-11', '10h00', 'Reel', '3 cosas para configurar en WhatsApp Business', R + 'dia26-reel-whatsapp-business.mp4',
  '3 cosas que tenés que configurar en tu WhatsApp Business hoy ✦\n1. El catálogo\n2. Las respuestas rápidas\n3. El mensaje de ausencia\n\nGuardalo y hacelo esta semana.\n\n#whatsappbusiness #emprendedorasargentinas #marketingdigital',
  None),
 ('Mar 03-11', '18h00', 'Carrusel', 'Lo que tiene que tener la etiqueta de tu producto', C + 'dia27-carrusel-etiqueta-de-tu-producto',
  'Lo que tiene que tener la etiqueta de tu producto ✦\nLogo visible, qué es, los datos, cómo encontrarte y una familia que combine.\n\n(Monte Dulce es una marca de ejemplo.)\nGuardalo para cuando diseñes la tuya.\n\n#packaging #diseñografico #emprendedorasargentinas',
  None),
 ('Mie 04-11', '10h00', 'Reel', 'POV: la propuesta a tu clienta', R + 'dia27-reel-pov-propuesta.mp4',
  'POV: le mostrás la propuesta a tu clienta ✦\nLogo con personaje, colores, patrón y cómo se ve en la vida real.\n\nY después llega ese mensaje que hace que todo valga la pena.\n(Huellitas es una marca de ejemplo.)\n\n#branding #diseñodelogos #emprendedorasargentinas', None),
 ('Jue 05-11', '18h00', 'Carrusel', 'Lo que tiene que tener tu página web', C + 'dia28-carrusel-que-tiene-que-tener-tu-web',
  'Lo que tiene que tener tu página web ✦\nInicio claro, servicios, quién sos, opiniones y un contacto fácil.\n\n¿A la tuya le falta alguna? Guardalo.\n\n#paginaweb #diseñoweb #marketingdigital', None),
 ('Vie 06-11', '10h00', 'Reel', 'El kit para arrancar tu marca', R + 'dia29-reel-kit-para-arrancar-tu-marca.mp4',
  'El kit para arrancar tu marca ✦\nLogo con variantes, paleta, perfil ordenado, página web, WhatsApp Business y plantillas para redes.\n\n¿Cuántas ya tenés? Contame abajo.\n\n#branding #emprendedorasargentinas #marketingdigital',
  None),
 ('Sab 07-11', '10h00', 'Carrusel', 'Qué necesito para arrancar tu proyecto', C + 'dia30-carrusel-que-necesito-para-arrancar',
  'Qué necesito para arrancar tu proyecto ✦\nTu marca, lo que ya tenés, ejemplos que te gusten y para cuándo lo necesitás. El resto lo armamos juntas.\n\nEscribime: el catálogo está en el link de la bio.\n\n#emprendedorasargentinas #branding #paginaweb', None),
]
out = F + 'GOLD-STUDIO-25-OCT-AL-7-NOV.zip'
cal = ['GOLD STUDIO · CALENDARIO DEL 25 DE OCTUBRE AL 7 DE NOVIEMBRE', '',
       'Abrí la carpeta del día, subí el archivo y copiá el texto de "texto.txt".',
       'Reels: agregales un audio en tendencia. Carruseles: subí las fotos en orden.',
       'Las marcas de los ejemplos son inventadas (así lo aclara cada texto).', '']
with zipfile.ZipFile(out, 'w') as z:
    for i, (d, h, fmt, title, src, txt, falta) in enumerate(POSTS, 1):
        tag = ' - FALTA' if falta else ''
        folder = f'GOLD-STUDIO-25-OCT-AL-7-NOV/{i:02d} - {d} - {h} - {fmt}{tag}/'
        cal.append(f'{i:02d}. {d} · {h.replace("h", ":")} h · {fmt:8} · {title}' + ('  (FALTA: tus fotos)' if falta else ''))
        z.writestr(folder + 'texto.txt', txt + '\n')
        if falta: z.writestr(folder + 'FALTA.txt', falta + '\n')
        if src and os.path.isdir(src):
            for f in sorted(glob.glob(src + '/*.png')): z.write(f, folder + os.path.basename(f))
        elif src: z.write(src, folder + 'reel.mp4')
    z.writestr('GOLD-STUDIO-25-OCT-AL-7-NOV/00 - CALENDARIO.txt', '\n'.join(cal) + '\n')
print(out)

# ---------- historias ----------
H = F + 'historias/semana2/'
DAYS = [('lun19', '01 - Lun 19-10'), ('mar20', '02 - Mar 20-10'), ('mie21', '03 - Mie 21-10'), ('jue22', '04 - Jue 22-10'), ('vie23', '05 - Vie 23-10'), ('sab24', '06 - Sab 24-10'), ('dom25', '07 - Dom 25-10')]
GUIA = '''HISTORIAS · SEMANA DEL 19 AL 25 DE OCTUBRE
Subí las de cada día en orden (1, 2, 3). Los espacios vacíos son para tus stickers. Los emojis ponelos vos.
Si sacaste tus fotos, podés usarlas en lugar de los dibujos (app, escritorio, boceto, web).

LUN 19 · Reel "Le hice una app a mi tía"
 1-app-tia      → va sola (o con tu foto del celu con la app).
 2-reel         → compartí el reel encima (avioncito > Agregar a tu historia).
 3-encuesta     → ENCUESTA: "Sí" / "Contame más".

MAR 20 · Carrusel "5 apps gratis"
 1-apps         → va sola (o tu foto del escritorio).
 2-quiz         → sticker QUIZ: Canva / CapCut / Notion / Pinterest.
 3-carrusel     → compartí el carrusel encima.

MIÉ 21 · Reel "Si sos nutri, psicóloga o entrenadora"
 1-preguntas    → CAJA DE PREGUNTAS en el espacio vacío.
 2-reel         → compartí el reel encima.
 3-respuesta    → para cada pregunta: compartila arriba y escribí tu respuesta en el recuadro.

JUE 22 · Carrusel "¿Página web o Linktree?"
 1-web          → va sola (o tu grabación de pantalla de la web).
 2-encuesta     → ENCUESTA: "Sí" / "No" / "Uso Linktree".
 3-carrusel     → compartí el carrusel encima.

VIE 23 · Reel "POV: el logo final"
 1-boceto       → va sola (o tu foto dibujando).
 2-slider       → SLIDER de emoji en el espacio vacío.
 3-reel         → compartí el reel encima.

SÁB 24 · Carrusel "Paquetes"
 1-agenda       → va sola.
 2-pocos        → va sola.
 3-catalogo     → sticker ENLACE: https://wa.me/c/5491171361309

DOM 25 · Cierre de la semana
 1-semana       → va sola (o tus clips del día).
 2-aprendi      → va sola.
 3-que-ver      → CAJA DE PREGUNTAS o ENCUESTA.
'''
out2 = F + 'historias-semana-19-al-25.zip'
with zipfile.ZipFile(out2, 'w') as z:
    z.writestr('historias-19-al-25/00-COMO-USARLAS.txt', GUIA)
    for pre, folder in DAYS:
        for f in sorted(glob.glob(H + pre + '-*.png')):
            z.write(f, f'historias-19-al-25/{folder}/' + os.path.basename(f)[len(pre) + 1:])
print(out2)
