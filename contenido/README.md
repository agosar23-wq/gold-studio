# Contenido de Gold Studio

Herramientas para hacer los posteos, reels, carruseles e historias de @goldstudio.ba.
No forma parte de la página web.

## Para una sesión nueva

```
bash contenido/setup.sh <scratchpad de la sesión>
```

Después se usa todo igual:

- `scripts/reelgen.py`: reels animados con sonidos (`build(nombre, escenas)`), a 30 fps, en mp4.
- `scripts/caro_ejemplos.py`: carruseles de 1080×1350 (`render(nombre, láminas, css_extra)`).
- `scratch/stories.py` (y `stories2..5.py`): historias de 1080×1920 sin emojis, con espacios vacíos para stickers.
- `scripts/catalogo_wa3.py`: catálogo de WhatsApp Business (5 servicios × 4 imágenes de 1080×1080) con fotos reales de Pexels.
  Las fotos están en `scratch/fotos-pexels/` (el nombre es el id: pexels.com/photo/<id>) y las imágenes listas en `salidas/whatsapp-business/catalogo/`.
- `scripts/marcas_ejemplo.py`: 4 marcas inventadas (Almendra, Ondina, Nácar, Nube) con logos en PNG transparente.
- `scripts/mockups_marcas.py`: pega esos logos sobre fotos de Pexels de productos en blanco (`scratch/mock/src/`), con perspectiva y textura.
- `scripts/carrusel_branding.py`: carrusel "¿Logo o branding?" con las 4 marcas (salida en `salidas/carruseles/logo-o-branding/`, con el texto del posteo).
- `scripts/mocks.py`, `pack.py`, `mascota.py`, `yogi.py`, `ilus_cafe.py`: dibujos y maquetas reutilizables.
- `scripts/semana*.py`: lo que ya se publicó, como ejemplo.
- `marca/`: logos, foto de perfil y paleta.

## Marca

- Colores: marfil `#FAF6EE`, negro `#1C1A17`, dorado `#B8923A` y `#C9A34E`.
- Letras: Bodoni Moda para títulos y Jost para textos.

## Reglas de Agos

- Ella no graba ni pone la voz: todo es animado o con ilustraciones.
- Carruseles siempre con ejemplos visuales; nada de solo texto.
- Historias sin emojis (los pone ella) y con espacio libre para stickers.
- Hasta 3 hashtags por posteo.
- No mostrar el nombre de la tía ni de su consultorio, solo el logo.
- No poner que las marcas de ejemplo son inventadas (ni en las imágenes ni en el texto).
- Reels a la velocidad original (no más rápidos) y con sonidos que se escuchen.
- Horarios: reels 10:00, carruseles 18:00, domingos 18:30.
