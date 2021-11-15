import numpy as np
from PIL import Image, ImageTk

#Get the pixel values from the image
def getPixels(image):
    width, height = image.size
    flatPixels = list(image.getdata())
    pixels = [flatPixels[i * width:(i + 1) * width] for i in range(height)]
    return pixels

#Get the image from the pixel values
def getImage(pixels):
    pixelsArray = np.asarray(pixels, np.uint8)
    return Image.fromarray(pixelsArray)

#Rotate the image clockwise
def rotateClockwise(image):
    pixels = getPixels(image)
    if len(pixels) == 0 or len(pixels[0]) == 0:
        return
    width, height = image.size
    
    finalPixels = []
    for row in range(width):
        rowPixels = [pixels[i][row] for i in range(height - 1, -1, -1)]
        finalPixels.append(rowPixels)
    return getImage(pixels)

#Rotate the image anticlockwise
def rotateAnticlockwise(image):
    pixels = getPixels(image)
    if len(pixels) == 0 or len(pixels[0]) == 0:
        return
    width, height = image.size

    finalPixels = []
    for row in range(width - 1, -1, -1):
        rowPixels = [pixels[i][row] for i in range(height)]
        finalPixels.append(rowPixels)
    return getImage(pixels)

fileName = input()
image = Image.open(f'D:\\{fileName}.png', 'r')
#image = rotateAnticlockwise(image)
#image.show()

red = (192, 80, 77, 255)
blue = (79, 129, 189, 255)

rC = bC = 0
for i in image.getdata():
    if i == red:
        rC += 1
    elif i == blue:
        bC += 1
print(rC, bC)
