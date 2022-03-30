"""
Post-processing of the results.
"""

import os
import shutil
from PIL import Image, ImageFont, ImageDraw

from strformat import StrFormat

def recheck(path: str, total: list[list[str]]):
    StrFormat.info("Checking the results...")
    t = len(total)
    ref = list(range(t))
    imgs = os.listdir(path)
    ind = []
    for img in imgs:
        ind.append(int(img.split("_")[0]))
    res_ind = [] # those indexs that don't have a qrcode
    for r in ref:    
        if r not in ind:
            res_ind.append(r)
    res = [",".join(total[r]) + '\n' for r in res_ind]
    with open("./failure.txt", "w+", encoding="utf-8") as f:
            f.writelines(res)
    StrFormat.ok("Failed results successfully written to ./failure.txt.")

UPRIGHT = [20, 20]

def attch_addr(path: str, total:list[list[str]]):
    StrFormat.info("Attaching addresses...")
    addrs = [t[2] for t in total]
    imgs = os.listdir(path)
    ind = []
    for img in imgs:
        ind.append(int(img.split("_")[0]))
    for i, dir in zip(ind, imgs): # main body here
        addr = addrs[i]
        addr = addr[addr.rfind("号") + 1:-1] # Room xxx
        img = Image.open(f"{path}/{dir}")
        # adds the addr to the upright of the image
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 20)
        draw.text(UPRIGHT, addr, font=font, fill=(0, 0, 0))
        img.save(f"./post_labels/{dir}")
    StrFormat.ok("Image attachment complete. Target dir: ./post_labels")
    
def clear(path: str):
    StrFormat.info("Clearing the labels...")
    shutil.rmtree(path)
    os.mkdir(path)
    StrFormat.ok("Clearing complete.")

