for _ in range(int(input())):
	n = int(input())
	a = list(map(abs, map(int, input().split())))
	print(max(0, 2 * (max(a[1::2]) - min(a[::2]))) + sum(a[::2]) - sum(a[1::2]) if n > 1 else a[0])
