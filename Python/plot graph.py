import matplotlib.pyplot as plt
x, y = [], []
for i in range(int(input())):
    l = input().split()
    x.append(float(l[-2]))
    y.append(float(l[-1]) ** 2)
plt.plot(x, y)
plt.show()
