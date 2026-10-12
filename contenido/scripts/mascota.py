"""Mascota de ejemplo: perrito sentado con pelota (línea fina continua)."""
def dog(color, size, bg=None, sw=None):
    sw = sw or (5.5 if size >= 300 else 8 if size >= 120 else 11)
    return (f'<svg width="{size}" height="{size}" viewBox="60 60 620 680" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">'
            # cabeza y mechón
            '<path d="M268 160 C300 132 335 118 362 122 M392 122 C430 124 465 136 490 160"/>'
            '<path d="M352 124 C362 112 368 102 376 94 C378 106 382 116 394 122"/>'
            # orejas
            '<path d="M268 160 C222 176 178 228 172 280 C168 322 198 368 234 384 C258 393 270 370 264 330 C260 292 262 246 270 206"/>'
            '<path d="M490 160 C532 176 574 212 584 252 C594 292 574 330 548 334 C526 337 514 310 510 280 C506 252 500 220 492 196"/>'
            # cara inferior
            '<path d="M266 342 C284 378 330 396 380 396 C430 396 482 376 506 330"/>'
            # ojitos cerrados, nariz y boca
            '<path d="M310 292 C318 274 342 272 354 290 M428 266 C438 250 462 250 470 266"/>'
            f'<path d="M386 314 C390 300 424 299 430 311 C433 324 416 337 406 337 C395 337 383 327 386 314 Z" fill="{color}"/>'
            '<path d="M406 337 C402 360 380 374 358 366 M406 337 C414 357 440 361 458 344"/>'
            # cuerpo
            '<path d="M302 398 C270 450 240 500 226 560 C214 616 220 662 246 690"/>'
            '<path d="M478 396 C494 460 500 530 496 600 C493 640 492 668 490 692"/>'
            # pata trasera
            '<path d="M248 532 C290 540 306 592 304 640 C302 664 300 680 300 692"/>'
            '<path d="M228 704 C228 686 286 682 298 700 C302 712 288 716 266 716 C242 716 228 714 228 704 Z"/>'
            '<path d="M256 710 l0 -10 M274 710 l0 -10"/>'
            # patas delanteras
            '<path d="M388 530 C394 600 394 650 390 692 M412 530 C418 600 418 650 414 692"/>'
            '<path d="M302 694 C298 716 394 718 392 694 M410 694 C406 716 494 718 492 694"/>'
            '<path d="M330 708 l0 -12 M356 708 l0 -12 M440 708 l0 -12 M464 708 l0 -12"/>'
            # cola
            '<path d="M218 608 C176 600 140 560 122 506 C118 494 130 490 134 500 C144 540 172 576 222 588"/>'
            # pelota
            '<circle cx="576" cy="656" r="54"/><path d="M532 628 C560 642 576 676 568 708 M590 604 C592 632 610 652 628 660"/>'
            '</svg>')

def paw(c, s=34, r=0):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 40 40" style="transform:rotate({r}deg)"><ellipse cx="20" cy="27" rx="9" ry="7.5" fill="{c}"/>'
            f'<circle cx="8" cy="17" r="4" fill="{c}"/><circle cx="15" cy="10" r="4" fill="{c}"/><circle cx="25" cy="10" r="4" fill="{c}"/><circle cx="32" cy="17" r="4" fill="{c}"/></svg>')
