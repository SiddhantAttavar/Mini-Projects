from random import randrange
class Account:
	def __init__(self, name):
		self.name = name
		self.balance = 0
		self.acc_no = randrange(0, int(1e18))
		self.account_summary()
	
	def deposit(self, amount):
		self.balance += amount
		print(f'Balance: {self.balance}')
	
	def withdraw(self, amount):
		self.balance -= amount
		print(f'Balance: {self.balance}')
	
	def account_summary(self):
		print(f'Name: {self.name}\nBalance: {self.balance}\nAccount No. {self.acc_no}')

accounts = {}
while True:
	op = input('Enter operation: Create account(C)/Withdraw (W)/Deposit (D)/Account summary(A)/Exit(E): ')
	if op == 'E':
		print('Thank you')
		break
	elif op == 'C':
		account = Account(input('Enter name: '))
		accounts[account.acc_no] = account
	elif op in 'WDA':
		acc_no = int(input('Enter account no.: '))
		if acc_no not in accounts:
			print('Account not found\n')
			continue

		if op == 'W':
			accounts[acc_no].withdraw(int(input('Enter amount to withdraw: ')))
		elif op == 'D':
			accounts[acc_no].deposit(int(input('Enter amount to deposit: ')))
		elif op == 'A':
			accounts[acc_no].account_summary()
	else:
		print('Invalid operation')
	print()
