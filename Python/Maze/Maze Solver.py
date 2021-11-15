from PIL import Image
from numpy import array, asarray, uint8
from importlib import import_module
from time import time

def imageTrim(image):
	up = 0
	down = 0
	left = 0
	right = 0

	for row in range(height):
		if not image[row][width // 4] and not image[row][width * 3 // 4]:
			up = row
			break

	for row in reversed(range(height)):
		if not image[row][width // 4] and not image[row][width * 3 // 4]:
			down = row
			break

	for col in range(width):
		if not image[height // 4][col] and not image[height * 3 // 4][col]:
			left = col
			break

	for col in reversed(range(width)):
		if not image[height // 4][col] and not image[height * 3 // 4][col]:
			right = col
			break

	newImage = []
	for row in range(up, down + 1):
		newImage.append(image[row][left: right + 1])

	return newImage

def getStartEndPoint(image):
	start = (-1, -1)

	for i in range(width):
		if image[0][i] == 0:
			if start == (-1, -1):
				start = (0, i)
				break
			else:
				return start, (0, i)
	
	for i in range(height):
		if image[i][0] == 0:
			if start == (-1, -1):
				start = (i, 0)
				break
			else:
				return start, (i, 0)
	
	for i in range(height):
		if image[i][width - 1] == 0:
			if start == (-1, -1):
				start = (i, width - 1)
				break
			else:
				return start, (i, width - 1)
	
	for i in range(width):
		if image[height - 1][i] == 0:
			if start == (-1, -1):
				start = (height - 1, i)
				break
			else:
				return start, (height, i)

def displayImage(image, path, title):
	pixels = [[(0, 0, 0, 0)] * width for _ in range(height)]

	for y in range(height):
		for x in range(width):
			pixels[y][x] = [image[y][x] * 255] * 3 + [0]

	for x, y in path:
		pixels[y][x] = [255, 0, 0, 0]

	print(path)

	finalImage = Image.fromarray(uint8(asarray(pixels, dtype = uint8)))
	
	finalImage.show(title)

	if input('Do you want to save this image? Y/N: ').strip().upper() == 'Y':
		finalImage.save(format = 'png')

#Get the image and pixels
fileName = f'maze {input("Enter the maze no. (1 - 9): ").strip()}'
imageFile = Image.open(f'mazes\\{fileName}.png').convert('L')
width, height = imageFile.size

#Get the pixel values
image = list(imageFile.getdata())
maze = []
for i in range(0, len(image), width):
	maze.append(image[i: i + width])

#Convert to black and white
maze = imageTrim(maze)
maze = array(maze)

maze[maze < 128] = 1
maze[maze >= 128] = 0

width, height = len(maze[0]), len(maze)
start, end = getStartEndPoint(maze)

while True:
	algorithName = input('Enter the algorithm you want to run: ').strip().upper()
	try:
		algorithm = import_module(f'Algorithms.{algorithName}')

		runTime = time()
		result = algorithm.solve(maze, start, end)
		runtime = (runTime - time()) * 1000

		#print(result)

		title = f'Result for {algorithName}:\nNumber of steps: {len(result)}\nTime: {runTime:.2f}'
		displayImage(maze, result, title)
	except ModuleNotFoundError as moduleNotFoundError:
		print('The algorithm name is invalid')

	if input('Do you want to run again? Y/N: ').strip().upper() == 'N':
		break
