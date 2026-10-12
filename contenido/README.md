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
- `scripts/mocks.py`, `pack.py`, `mascota.py`, `yogi.py`, `ilus_cafe.py`: dibujos y maquetas reutilizables.
- `scripts/personaje_cafe.py`: personas adultas en salvavidas, ilustración de línea, para poner sobre fotos de café (poses: brindis, relax, mano_agua).
- `scripts/semana*.py`: lo que ya se publicó, como ejemplo.
- `marca/`: logos, foto de perfil y paleta.
- `scratch/pexels/`: fotos reales de Pexels (cafetería) que usa `carrusel_feed_cafe.py`.
- `carruseles/`: láminas terminadas y su texto para el posteo.

## Marca

- Colores: marfil `#FAF6EE`, negro `#1C1A17`, dorado `#B8923A` y `#C9A34E`.
- Letras: Bodoni Moda para títulos y Jost para textos.

## Reglas de Agos

- Ella no graba ni pone la voz: todo es animado o con ilustraciones.
- Carruseles siempre con ejemplos visuales; nada de solo texto.
- Historias sin emojis (los pone ella) y con espacio libre para stickers.
- Hasta 3 hashtags por posteo.
- No mostrar el nombre de la tía ni de su consultorio, solo el logo.
- Las marcas de ejemplo se aclaran en el texto.
- Reels a la velocidad original (no más rápidos) y con sonidos que se escuchen.
- Horarios: reels 10:00, carruseles 18:00, domingos 18:30.
