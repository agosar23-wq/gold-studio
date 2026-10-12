import sys
sys.path.insert(0, '/home/user/gold-studio-contenido')
from reelgen import build, SCR
A = f'file://{SCR}/appshots/'
REELS = {
 'dia01-reel-marca-improvisada': [
   dict(bg='n', text='3 señales de que tu marca parece *improvisada*'),
   dict(bg='m', eb='Señal 1', text='Cada posteo tiene *colores distintos*', sub='Tu cerebro no sabe qué es tuyo.', deco='swatches'),
   dict(bg='m', eb='Señal 2', text='Usás *cinco* tipografías', sub='Con dos alcanza.', deco='fonts'),
   dict(bg='m', eb='Señal 3', text='Tu foto de perfil *no se entiende* en chiquito', sub='Y es lo primero que ven.', deco='avatar'),
   dict(bg='g', kind='end', text='¿Tenés las tres? *Todo tiene arreglo.*', pill='Guardalo y revisalo hoy'),
 ],
 'dia03-reel-pagina-web-o-instagram': [
   dict(bg='n', text='¿Necesitás *página web* si ya tenés Instagram?'),
   dict(bg='m', text='Te digo algo que a muchas diseñadoras no les conviene: *no siempre.*'),
   dict(bg='m', eb='Todavía no', text='Si recién arrancás, con Instagram ordenado y WhatsApp *estás bien.*'),
   dict(bg='m', eb='Ahí sí', text='Si te buscan en Google, querés turnos o pagos online, o verte *más profesional.*'),
   dict(bg='n', text='Instagram es un local que *no es tuyo.* Tu página es *tu casa.*'),
   dict(bg='g', kind='end', text='¿En qué etapa estás *vos?*', pill='Contame en comentarios'),
 ],
 'dia05-reel-asi-nacio-mi-logo': [
   dict(bg='n', text='Cambié el nombre de mi marca *3 veces*'),
   dict(bg='m', kind='strike', eb='Primero', strike='AR Studio', text='Muy *genérico.*'),
   dict(bg='n', kind='strike', eb='Después', strike='<img src="file:///home/user/magma-logo/logo-magma-creations-blanco.png">', text='Lava chorreando y todo, *jaja.*'),
   dict(bg='m', text='Probé gotas, rosas, mil colores... y *nada era yo.*'),
   dict(bg='m', kind='logo', text='Hasta que apareció *Gold.*', dur=3.4),
   dict(bg='g', kind='end', text='Tu marca tiene que *sentirse tuya.*', pill='¿Te pasó lo mismo?'),
 ],
 'dia07-reel-todo-empezo-con-mi-tia': [
   dict(bg='n', text='Todo empezó con una *app para mi tía*'),
   dict(bg='m', text='Ella es nutricionista y mandaba los planes *por WhatsApp.*', sub='Se perdía todo.'),
   dict(bg='m', kind='phone', img=A + 'p-inicio.png', text='Le hice una app: cada paciente con *su cuenta.*', fs=88),
   dict(bg='n', text='Cuando la vi usándola, supe que *esto era lo mío.*'),
   dict(bg='g', kind='end', text='Así nació *Gold Studio.*', pill='Gracias por estar desde el día uno'),
 ],
}
which = sys.argv[1:] or list(REELS)
for n in which:
    out, total, work = build(n, REELS[n])
    print(n, total, work)
