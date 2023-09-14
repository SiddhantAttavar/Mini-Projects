n = int(input())
res = [[-1] * n for _ in range(n)]
x, y = 0, 0
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
c = 1
for i in range(n * n - 1):
	res[y][x] = i + 1
	p, q = x + dir[c][0], y + dir[c][1]
	while min(p, q) < 0 or max(p, q) >= n or res[q][p] != -1:
		c = (c + 1) % 4
		p, q = x + dir[c][0], y + dir[c][1]
	x, y = p, q
res[y][x] = n * n
for i in res:
	print(*i)
