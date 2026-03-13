import numpy as np
from matplotlib import pyplot as plt

n = 100000

mean = 0
std = 2
k = np.exp(np.random.normal(mean, std, n))
t0 = 0.05
prob = 0.5
print(k)

# plt.hist(k, bins = 100)
# plt.show()

y = 0
x = int(1 * n)

c = 0
data = [0]
time = [0]
while y < x:
	t = np.log((x - y) * k / (y + 1)) / (k + 1)
	p = np.random.random(k.shape) < prob
	c += 1
	mask = np.logical_and(t < t0, p)
	y += np.sum(mask)
	data.append(y / n * 100)
	time.append(np.average(t))
	k = k[~mask]
	print(c, y, x, np.average(t))
	assert(y + len(k) == n)
	if np.sum(t < t0) == 0:
		break
if y >= x:
	print('Event started')

d = [data[i] - data[i - 1] for i in range(1, len(data))]
plt.plot(d)
# plt.plot(data)
plt.xlabel('Time steps')
plt.ylabel('Incoming people (as percentage)')
# plt.plot(time)
plt.show()
