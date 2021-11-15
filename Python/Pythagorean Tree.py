import math 
from tkinter import *   
alfa=math.pi/3
def Pyth_tree( x, y, side, fi, alfa, deep, count_deep):
    dx,dy=side*math.sin(fi),side*math.cos(fi)
    x1,y1=x+dx,y-dy   
    x2,y2=x+dx-dy,y-dy-dx
    x3,y3=x-dy,y-dx
    x4=x-dy+side*math.cos(alfa)*math.sin(fi-alfa)
    y4=y-dx-side*math.cos(alfa)*math.cos(fi-alfa)
    if count_deep<5: colour="#"+str(count_deep*20)+"0000"
    elif count_deep<9: colour="#00"+str(count_deep*10)+"00"
    else: colour="#0000"+str(count_deep*5)
    canv.create_polygon(x, y, x1, y1, x2, y2, x3, y3, fill=colour)
    canv.create_polygon(x3, y3, x2, y2, x4, y4, fill=colour)
    if deep>1:
        Pyth_tree(x4, y4, side*math.sin(alfa), fi-alfa+math.pi/2, alfa, deep-1,count_deep+1)
        Pyth_tree(x3, y3, side*math.cos(alfa), fi-alfa, alfa, deep-1,count_deep+1)
depth = int(input('Enter the number of levels: '))
root=Tk()
root.title("Pythagorean tree")
canv = Canvas(root, width = 1600, height = 1200, bg = "lightgreen")
canv.pack()
Pyth_tree(650, 650, 100, math.pi/2, alfa*3/4, depth, 1) 
root.mainloop()
