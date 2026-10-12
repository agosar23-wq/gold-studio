#!/usr/bin/env bash
# Prepara una sesión nueva para seguir haciendo el contenido de Gold Studio.
# Uso: bash contenido/setup.sh /ruta/del/scratchpad
set -euo pipefail
NEW="${1:?Pasá la ruta del scratchpad de la sesión}"
OLD="/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad"
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$NEW/logo/node_modules/@fontsource" /home/user/gold-studio-contenido /home/user/gold-studio-final/reels /home/user/gold-studio-final/carruseles /home/user/gold-studio-final/historias
cp -r "$HERE/scripts/." /home/user/gold-studio-contenido/
cp -r "$HERE/scratch/." "$NEW/"
cp -r "$HERE/scratch/fonts/." "$NEW/logo/node_modules/@fontsource/"
cp -r "$HERE/marca/." /home/user/gold-studio-final/
grep -rlF "$OLD" /home/user/gold-studio-contenido "$NEW" --include='*.py' --include='*.js' | xargs -r sed -i "s#$OLD#$NEW#g"
pip install -q numpy imageio-ffmpeg pillow 2>/dev/null || true
echo "Listo: scripts en /home/user/gold-studio-contenido, recursos en $NEW, salidas en /home/user/gold-studio-final"
