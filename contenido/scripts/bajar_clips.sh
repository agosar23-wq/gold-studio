#!/usr/bin/env bash
# Baja los clips de Pexels (cottonbro, mismo café) que usa reel_cafe.py. Necesita videos.pexels.com permitido en la red.
# Uso: bash bajar_clips.sh /ruta/del/scratchpad
set -euo pipefail
D="${1:?Pasá la ruta del scratchpad}/clips"; mkdir -p "$D"
for c in 4796951:hd_1080_2048 4795024:hd_2048_1080 4796954:hd_2048_1080 4796959:hd_2048_1080 4795018:hd_2048_1080 \
         4795015:hd_1080_2048 4796949:hd_1080_2048 4796962:hd_1080_2048 4795016:hd_2048_1080; do
  id=${c%%:*}; sz=${c##*:}
  [ -f "$D/$id.mp4" ] || curl -sS -f -o "$D/$id.mp4" "https://videos.pexels.com/video-files/$id/$id-${sz}_25fps.mp4"
done
# Hamburguesería (Los Muertos Crew, misma parrilla) para reel_hamburguesas.py
B="${1}/bclips"; mkdir -p "$B"
for c in 8477334:hd_1920_1080_24 8477263:hd_1920_1080_24 8477404:hd_1920_1080_24 8477267:hd_1920_1080_24 8477262:hd_1080_1920_24 \
         8477405:hd_1920_1080_24 8477403:hd_1080_1920_24 8477333:hd_1080_1920_24 8477329:hd_1920_1080_24 8477408:hd_1080_1920_24 8477410:hd_1920_1080_24; do
  id=${c%%:*}; v=${c#*:}
  [ -f "$B/$id.mp4" ] || curl -sS -f -o "$B/$id.mp4" "https://videos.pexels.com/video-files/$id/$id-${v}fps.mp4"
done
echo "Clips en $D y $B"
