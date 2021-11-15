from math import factorial
from random import shuffle

def probability(n):
	dp = [1]
	
	currSum = 1
	for i in range(2, n // 2 + 1):
		dp.append(currSum)
		currSum += dp[-1]
	
	removeSum = 1
	for i in range(n // 2 + 1, n + 1):
		dp.append(currSum - removeSum)
		currSum += dp[-1]
		removeSum += dp[i - n // 2]
	
	return dp[-1] / factorial(n)

def sample():
	shuffle(cards)
	for i in range(n):
		curr = i
		for _ in range(n // 2):
			curr = cards[curr]
			if curr == i:
				break
		else:
			return False
	return True


n = int(input('Enter the number of prisoners: '))
cards = list(range(n))

totalSamples = 1000
numSuccesfull = 0
for _ in range(totalSamples):
	if sample():
		numSuccesfull += 1

print(f'The probability is : {numSuccesfull / totalSamples * 100:.2f}%')
print(f'The probability is : {probability(n) * 100:.2f}%')