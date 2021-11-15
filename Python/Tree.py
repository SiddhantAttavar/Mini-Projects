from tkinter import *
from math import sqrt
from collections import defaultdict
r2 = sqrt(2)
done = defaultdict(lambda: set())
def drawSquare(x, y, a):
    hs = a / 2
    canvas.create_polygon([x - hs, y - hs, x + hs, y - hs, x + hs, y + hs, x - hs, y + hs])
def drawSquareTilted(x, y, a):
    hd = a / r2
    canvas.create_polygon([x - hd, y, x, y - hd, x + hd, y, x, y + hd])
def draw(x, y, a, d, dir):
    if d == depth: return
    if y in done[x]: return
    done[x].add(y)
    ar2 = a / r2
    d += 1
    if d % 2 == 1:
        drawSquare(x, y, a)
        a2 = a / 2
        if dir == 0:
            draw(x-a/2, y+a, ar2, d, 3)
            draw(x+a/2, y+a, ar2, d, 0)
        elif dir == 1:
            draw(x-a, y+a2, ar2, d, 0)
            draw(x-a, y-a2, ar2, d, 1)
        elif dir == 2:
            draw(x-a2, y-a, ar2, d, 1)
            draw(x+a2, y-a, ar2, d, 2)
        else:
            draw(x+a, y-a2, ar2, d, 2)
            draw(x+a, y+a2, ar2, d, 3)
    else:
        drawSquareTilted(x, y, a)
        diff = ar2 / 2
        if dir == 0:
            draw(x - diff, y + diff * 3, ar2, d, 0)
            draw(x - diff * 3, y + diff, ar2, d, 1)
        elif dir == 1:
            draw(x - diff * 3, y - diff, ar2, d, 1)
            draw(x - diff, y - diff * 3, ar2, d, 2)
        elif dir == 2:
            draw(x + diff, y - diff * 3, ar2, d, 2)
            draw(x + diff * 3, y - diff, ar2, d, 3)
        else:
            draw(x + diff * 3, y + diff, ar2, d, 3)
            draw(x + diff, y + diff * 3, ar2, d, 0)
    
root = Tk()
canvas = Canvas(root, width = 1500, height = 1200, bg = "lightgreen")
canvas.pack(expand=YES, fill=BOTH)
depth = int(input())
draw(650, 650, 100, 0, 2)
root.mainloop()
