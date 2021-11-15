from re import findall
from random import randint, choice

n = int(input('Enter the password length: '))
if n < 3:
	raise ValueError('Password Length too small')

pwd = [-1] * n

numbers = ''
alphabets = ''
symbols = ''
for i in range(72):
	if i >= ord('0') and i <= ord('9'):
		numbers += chr(i)
	elif (i >= ord('a') and i <= ord('z')) or (i >= ord('A') and i <= ord('Z')):
		alphabets += chr(i)
	else:
		symbols += chr(i)

num = randint(0, n - 1)
pwd[num] = choice(numbers)

alpha = randint(0, n - 1)
while alpha == num:
	alpha = randint(0, n - 1)
pwd[alpha] = choice(alphabets)

sym = randint(0, n - 1)
while sym == num or sym == alpha:
	sym = randint(0, n - 1)
pwd[sym] = choice(symbols)

for i in range(n):
	if i not in {num, alpha, sym}:
		pwd[i] = chr(randint(0, 71))

print(f'Your password is: {"".join(pwd)}')