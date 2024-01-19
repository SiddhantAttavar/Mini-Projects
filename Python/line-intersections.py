from functools import cache

def visualize(s):
	from matplotlib import pyplot as plt
	x, y = zip(*s)
	plt.plot(x, y, 'ro-')
	plt.show()

def no_symmetry(x, n):
	return True
	x = 2 * x + 1
	v = [bool(x & (1 << j)) for j in range(n - 1)]
	# print(v)
	
	sym = [x]
	sym.append(0)
	for i in v:
		sym[-1] <<= 1
		sym[-1] += i

	if not v[-1]:
		sym[-1] ^= (1 << (n - 1)) - 1
	
	# print(x, *sym)
	return x == min(sym)

def solve(n):
	res = 0
	a = [(0, 1), (-1, 0), (0, -1), (1, 0)]
	sols = []
	for i in range(1 << (n-2)):
		x, y = 1, 1
		d = 3
		s = {(0,0),(0, 1), (1, 1)}
		l = [(0, 0), (0, 1), (1, 1)]
		for j in range(n-2):
			if i & (1 << j):
				d = (d + 3) % 4
			else:
				d = (d + 1) % 4
			x += a[d][0]
			y += a[d][1]
			# print(f"({x},{y})",end=' ')
			if (x, y) in s:
				break
			s.add((x, y))
			l.append((x, y))
		else:
			#if (x, y) not in s:
			# sols.append(l)
			if no_symmetry(i, n):
				sols.append(l)
				res += 1
	# print(sols)
	# for i in sols:
	# 	visualize(i)
	return res

def solve_rec(x, y, ):
	pass

@cache
def fib(n):
	if n <= 2:
		return 1
	return fib(n - 1) + fib(n - 2)

print('n\tFib\tActual')
for n in range(2, 22):
	x, y = fib(n), solve(n)
	print(n, x, y, sep = '\t')
	# if x != y:
	# 	print(n)
	# 	break
# print(f'Ans: {solve(21)}')
