inputFile = open('input.txt', 'r')
data = inputFile.readlines()
inputFile.close()

res = []
x = 0
d = {
	0: 0,
	1: 17,
	2: 16,
	3: 17,
	4: 50
}

for l in data:
	c = -1
	num = ''
	for i in range(len(l)):
		if l[i].isnumeric():
			if c == -1:
				c = i
			num += l[i]
	
	if not num:
		if l:
			res.append(l)
	else:
		out = str(int(num) - d[x])
		x = (x + 1) % 5
		res.append(l[:c] + out + l[c + len(num):])

outputFile = open('output.txt', 'w')
outputFile.writelines(res)
outputFile.close()
