inputFile = open('input.txt', 'r')
outputFile = open('output.csv', 'w')

score = int(input('Enter your NTSE score: '))

inputFile.readline()
inputFile.readline()
line = inputFile.readline()
res = [','.join(line.split()) + '\n']

finalList = []
while line:
	line = inputFile.readline()
	words = line.split()
	if len(words) > 0 and words[0].isnumeric() and words[-1].isnumeric():
		finalLine = words[:2] + [' '.join(words[2:-3])] + words[-3:]
		finalList.append(finalLine)

finalList = sorted(finalList, key = lambda x : -int(x[-1]))

count = 0
for i in finalList:
	res.append(','.join(i) + '\n')
	if int(i[-1]) > score:
		count += 1

print(f'{count} / {len(finalList)} scored above you in Karnataka. Check output.csv for more details')
input('Press Enter to exit: ')

outputFile.writelines(res)

inputFile.close()
outputFile.close()
