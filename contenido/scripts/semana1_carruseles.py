import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import render
C = {
 'dia02-carrusel-5-errores-instagram': [
  dict(bg='g', kind='cover', text='5 errores que hacen que tu Instagram parezca *poco profesional*', sub='El 4 lo hace casi todo el mundo.'),
  dict(kind='item', n=1, title='Foto de perfil que *no se lee* en chiquito', tip='Usá un ícono simple o tu logo, sin texto chiquito.'),
  dict(kind='item', n=2, title='Una bio que *no dice qué hacés*', tip='"Diseño páginas web para emprendedores" le gana a "Amo el café".'),
  dict(kind='item', n=3, title='Colores distintos *en cada posteo*', tip='Elegí 3 colores y repetilos siempre.'),
  dict(kind='item', n=4, title='Historias destacadas *sin portada*', tip='Con portadas iguales, tu perfil se ve ordenado al toque.'),
  dict(kind='item', n=5, title='No hay forma de *contactarte*', tip='Sumá el botón de WhatsApp o un link en la bio.'),
  dict(bg='n', kind='end', text='¿Cuántos tenías? *Todo tiene arreglo.*', pill='Guardalo y mandáselo a una amiga'),
 ],
 'dia04-carrusel-colores-de-tu-marca': [
  dict(bg='n', kind='cover', text='Qué transmite cada *color* en tu marca', sub='Elegí bien antes de hacer tu logo.'),
  dict(kind='color', title='Dorado', tip='Elegancia, valor, algo especial.', style='background:#C9A34E;color:#1C1A17'),
  dict(kind='color', title='Negro', tip='Lujo, seriedad, sofisticación.', style='background:#1C1A17;color:#FAF6EE'),
  dict(kind='color', title='Verde', tip='Salud, naturaleza, calma.', style='background:#5E7D5B;color:#FAF6EE'),
  dict(kind='color', title='Rosa', tip='Cercanía, dulzura, cuidado.', style='background:#E8B4B8;color:#3A1C1C'),
  dict(kind='color', title='Azul', tip='Confianza, profesionalismo, tranquilidad.', style='background:#2F4A6D;color:#FAF6EE'),
  dict(kind='color', title='Naranja', tip='Energía, alegría, algo accesible.', style='background:#E07A3F;color:#1C1A17'),
  dict(kind='text', eb='Tip', title='1 color principal, 1 secundario y *1 para detalles*', sub='Así tu marca se ve ordenada y se reconoce rápido.'),
  dict(bg='g', kind='end', text='¿Cuál es el color de *tu marca?*', pill='Contame en comentarios'),
 ],
 'dia06-carrusel-checklist-bio': [
  dict(bg='m', kind='cover', eb='Checklist', text='Tu bio tiene *3 segundos* para convencer', sub='¿Tiene todo esto?'),
  dict(kind='check', title='Qué hacés', sub='Claro y sin vueltas.'),
  dict(kind='check', title='Para quién lo hacés', sub='Emprendedoras, profesionales, mamás, pymes...'),
  dict(kind='check', title='Dónde estás', sub='Si trabajás en una zona o hacés envíos.'),
  dict(kind='check', title='Una invitación', sub='"Escribime por DM", "Pedí tu turno", "Comprá acá".'),
  dict(kind='check', title='Un link', sub='A tu WhatsApp, tu página o tu catálogo.'),
  dict(kind='quote', eb='Ejemplo', text='Diseño páginas web y marcas para emprendedores ✦ Buenos Aires ✦ Pedí tu presupuesto'),
  dict(bg='n', kind='end', text='Guardalo y *editá tu bio hoy.*', pill='@goldstudio.ba'),
 ],
}
for n in (sys.argv[1:] or C):
    print(render(n, C[n]))
