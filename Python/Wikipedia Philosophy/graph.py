from matplotlib import pyplot as plt
from main import main, maxVisits, randomPage

n = int(input('No. of samples: '))
y = [0] * maxVisits

i = 0
while i < n:
    try:
        res = main(randomPage)
        if res == -1:
            visited = -1
            print(-1)
            y[maxVisits] += 1
        else:
            visited = len(res)
            print(visited, res[0])
            y[visited - 1] += 1
        i += 1
    except:
        pass

plt.plot(range(1, maxVisits + 1), y)
plt.show()
