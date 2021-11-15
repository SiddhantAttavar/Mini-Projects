from tkinter import *
import math

def draw(a, b, c, level):
    global count, scale
    
    if level == 1:
        count += 1
        drawTriangle(a, b, c)
        return
    
    base = b[0] - a[0]
    x = (a[0] + base * 3 / 4, a[1] + scale * base / 2)
    y = (a[0] + base / 4, a[1] + scale * base / 2)
    z = (a[0] + base / 2, a[1])

    level -= 1
    draw(a, z, y, level)
    draw(z, b, x, level)
    draw(y, x, c, level)

def drawTriangle(a, b, c):
    global canvas
    
    x = (a[0], size - a[1])
    y = (b[0], size - b[1])
    z = (c[0], size - c[1])
    canvas.create_polygon(x, y, z)

size = 500
side = size / 2

scale = math.sqrt(3) / 2

root = Tk()
root.title("Sierpinski Triangle Fractal")
canvas = Canvas(root, width = size, height = size, bg = "cyan")
canvas.pack()

a = (size / 4, size / 4)
b = (size / 4 + side, size / 4)
c = (size / 2, size / 4 + scale * side)

count = 0
levels = int(input())
draw(a, b, c, levels)

print('The number of triangles required is: ' + str(count))
print('It is ' + ('not ' if count != levels ** 2 else '') + 'equal to the number of levels ^ 2')

root.mainloop()
