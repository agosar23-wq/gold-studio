import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from reelgen import build, SCR
from mocks import chat, logo_card, moodboard
A = f'file://{SCR}/appshots/'
SW = '<div style="display:flex;gap:18px">' + ''.join(f'<i style="width:150px;height:150px;border-radius:50%;background:{c};box-shadow:inset 0 0 0 3px rgba(0,0,0,.06)"></i>' for c in ['#E8B4B8', '#FFF6F4', '#4A2329', '#C9A34E']) + '</div>'
FT = ('<div style="display:flex;flex-direction:column;gap:6px;font-size:96px;line-height:1.05;color:#4A2329">'
      '<span style="font-family:XArchivo;opacity:.35;text-decoration:line-through">Dulce Mía</span>'
      '<span style="font-family:XPlayfair;opacity:.35;text-decoration:line-through">Dulce Mía</span>'
      '<span style="font-family:B">Dulce Mía ✓</span></div>')
REELS = {
 'dia08-reel-app-para-mi-tia': [
   dict(bg='n', text='Le hice una app a mi tía nutricionista y *esto pasó*'),
   dict(bg='m', eb='Antes', html=chat(880, 1.45), html_pos='top', text='Planes perdidos y mensajes *a cualquier hora.*', fs=80),
   dict(bg='m', kind='phone', img=A + 'p-inicio.png', eb='Ahora', text='Cada paciente ve *su plan y su turno.*', fs=84),
   dict(bg='m', kind='phone', img=A + 'p-progreso.png', text='Y sigue *su progreso.*', fs=96),
   dict(bg='m', kind='phone', img=A + 'n-panel.png', text='Ella maneja todo desde *un panel.*', fs=88),
   dict(bg='g', kind='end', text='¿Tenés un negocio con *clientes fijos?*', pill='Probá la demo en la bio'),
 ],
 'dia10-reel-profesionales-whatsapp': [
   dict(bg='n', text='Si sos nutri, psicóloga o entrenadora y mandás todo *por WhatsApp...*'),
   dict(bg='m', html=chat(880, 1.45), html_pos='top', text='¿Te suena *esto?*', fs=110),
   dict(bg='m', text='Planes que se pierden y turnos anotados *en cualquier lado.*'),
   dict(bg='m', kind='phone', img=A + 'p-docs.png', text='Con una app propia, cada paciente tiene *sus archivos.*', fs=80),
   dict(bg='m', kind='phone', img=A + 'p-turnos.png', text='Y sus *turnos,* siempre a mano.', fs=90),
   dict(bg='n', text='Vos ganás tiempo. Tus pacientes te ven *más profesional.*'),
   dict(bg='g', kind='end', text='Mandáselo a esa colega con el *WhatsApp explotado*', pill='Compartilo'),
 ],
 'dia12-reel-pov-logo-final': [
   dict(bg='n', text='POV: le mostrás el logo final *a tu clienta*'),
   dict(bg='m', html=moodboard(860), html_pos='top', text='Después de semanas de *bocetos y pruebas...*', fs=86),
   dict(bg='m', kind='reveal', html=logo_card('dulce', 660), html_pos='top', text='...y se le llenan los ojos *de lágrimas*', fs=86),
   dict(bg='g', kind='end', text='Por esto hago *lo que hago.*', pill='Marca de ejemplo · @goldstudio.ba'),
 ],
 'dia14-reel-domingo-en-gold-studio': [
   dict(bg='n', text='Un domingo cualquiera en *Gold Studio*'),
   dict(bg='m', text='Mate, playlist tranqui y una *marca nueva* para armar.'),
   dict(bg='m', html=SW, text='Elijo *colores...*', fs=120),
   dict(bg='m', html=FT, text='Pruebo *tipografías...*', fs=120),
   dict(bg='m', html=moodboard(860), html_pos='top', text='Y cuando algo encaja, *se siente.*', fs=96),
   dict(bg='g', kind='end', text='¿Vos trabajás los domingos *o descansás?*', pill='Contame, jaja'),
 ],
}
for n in (sys.argv[1:] or list(REELS)):
    out, total, work = build(n, REELS[n]); print(n, total, work)
