from matplotlib import pyplot as plt
from csv import reader

file = open(f'{input("File name: ")}.csv', 'r')
data = reader(file)

xData = []
yData = []

for row in data:
    val = float(row[2])
    yData.append(val)

yData = yData[3: len(yData) // 8 + 3]
xData = list(range(len(yData)))

plt.plot(xData, yData)
plt.show()
