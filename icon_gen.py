# -*- coding: utf-8 -*-
"""Gera os icones PWA do Bolao (fundo navy gradiente + trofeu)."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.dirname(os.path.abspath(__file__))
TOP = (22, 35, 58)    # #16233a
BOT = (11, 18, 32)    # #0b1220
GOLD = (255, 211, 77) # #ffd34d

def make(size):
    img = Image.new('RGB', (size, size), BOT)
    d = ImageDraw.Draw(img)
    # fundo gradiente vertical
    for y in range(size):
        t = y / float(size)
        col = (int(TOP[0] + (BOT[0]-TOP[0])*t),
               int(TOP[1] + (BOT[1]-TOP[1])*t),
               int(TOP[2] + (BOT[2]-TOP[2])*t))
        d.line([(0, y), (size, y)], fill=col)
    # anel dourado sutil
    m = int(size*0.085)
    d.ellipse([m, m, size-m, size-m], outline=GOLD, width=max(3, size//64))
    # trofeu (emoji colorido) com fallback
    drawn = False
    try:
        fnt = ImageFont.truetype("C:/Windows/Fonts/seguiemj.ttf", int(size*0.56))
        d.text((size/2, size/2 + size*0.02), "\U0001F3C6", font=fnt, anchor="mm", embedded_color=True)
        drawn = True
    except Exception as e:
        print("emoji fallback:", e)
    if not drawn:
        # fallback: taca desenhada
        cx = size/2
        cup_w = size*0.42; cup_h = size*0.30; top_y = size*0.28
        d.pieslice([cx-cup_w/2, top_y, cx+cup_w/2, top_y+cup_h*1.3], 0, 180, fill=GOLD)
        d.rectangle([cx-cup_w/2, top_y, cx+cup_w/2, top_y+cup_h*0.45], fill=GOLD)
        d.rectangle([cx-size*0.03, top_y+cup_h*1.1, cx+size*0.03, top_y+cup_h*1.7], fill=GOLD)
        d.rectangle([cx-size*0.12, top_y+cup_h*1.7, cx+size*0.12, top_y+cup_h*1.9], fill=GOLD)
    img.save(os.path.join(OUT, "icon-%d.png" % size))
    return size

for s in (512, 192, 180):
    print("ok", make(s))
print("done")
