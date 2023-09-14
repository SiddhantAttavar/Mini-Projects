l = list(map(int, input().split()))
a = []
for i in range(1 << len(l)):
	a.append([])
	for j in range(len(l)):
		if i & (1 << j):
			a[-1].append(l[j])
for i in a:
	print(*i)
