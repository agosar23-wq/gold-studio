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
echo "Clips en $D"
