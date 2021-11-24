from csv import reader, writer

# Read the input CSV file
inputFile = open('input.csv', 'r')
inputReader = reader(inputFile, lineterminator = '\n')
inputData = list(inputReader)

outputFile = open('output.csv', 'w')
outputWriter = writer(outputFile, lineterminator = '\n')
outputData = []

for row in inputData[2:]:
	curr = []
	for i in range(2, len(row), 4):
		curr.append(row[i: i + 4])
	sumScores = [0] * 3
	count = [0] * 3
	for i in range(len(curr)):
		curr[i][0] = int(curr[i][0])
		if curr[i][1] == '':
			continue
		for j in range(3):
			curr[i][j + 1] = int(curr[i][j + 1])
			sumScores[j] += int(curr[i][j + 1])
			count[j] += 1
	for i in range(len(curr)):
		if curr[i][1] == '':
			for j in range(3):
				curr[i][j + 1] = sumScores[j] / count[j]
			curr[i][0] = sum(curr[i][1:])
	curr = row[:2] + curr
	curr[1] = sum([i[0] for i in curr[2:]])
	outRow = curr[:2]
	for i in curr[2:]:
		outRow += i
	outputData.append(outRow)

outputData.sort(key = lambda x: x[1], reverse = True)

data = inputData[:2]
data += [[f'{i:.2f}' if type(i) == float else i for i in row] for row in outputData]
outputWriter.writerows(data)

inputFile.close()
outputFile.close()
