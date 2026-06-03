# -*- coding: utf-8 -*-
"""Gera icon-512/192/180 a partir da imagem enviada."""
from PIL import Image
import os

OUT = os.path.dirname(os.path.abspath(__file__))
src = Image.open(os.path.join(OUT, "iconI new.png")).convert("RGBA")

# center-crop para quadrado
w, h = src.size
s = min(w, h)
left = (w - s) // 2
top = (h - s) // 2
src = src.crop((left, top, left + s, top + s))

for size in (512, 192, 180):
    img = src.resize((size, size), Image.LANCZOS).convert("RGB")
    img.save(os.path.join(OUT, "icon-%d.png" % size), "PNG")
    print("ok", size)
print("done")
