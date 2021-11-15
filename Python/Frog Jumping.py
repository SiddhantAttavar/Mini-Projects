def solve(n):
	if n == 0:
		return 1 / 2

	dp = [(0, 1), (1, 1)]
	
	jumpSum = 1
	countSum = 2
	for i in range(2, n + 1):
		dp.append((jumpSum + countSum, countSum))
		countSum += dp[-1][1]
		jumpSum += dp[-1][0]

	return dp[-1][0] / dp[-1][1]

print(f'{solve(int(input("Enter the no. of lilypads: "))):.2f}')

for i in range(1000):
	if (solve(i) != (i + 1) / 2):
		print(f'Failed for n = {i}')