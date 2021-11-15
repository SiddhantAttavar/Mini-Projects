from random import randrange

def getInput(playerName):
    item = input(f'{playerName}\'s turn - Rock (R), Paper (P) or Scissors (S): ').upper()
    while item not in operations:
        item = input(f'Invalid Input\n{playerName}\'s turn - Rock (R), Paper (P) or Scissors (S): ').upper()
    return item

print('Welcome to Rock, Paper and Scissors')

playingComputer = input('Would you like to play against the computer? (Y\\N): ').upper() == 'Y'

if playingComputer:
    player1 = input('What is the name of the player? ')
    player2 = 'The computer'
else:
    player1 = input('What is the name of the 1st player? ')
    player2 = input('What is the name of the 2nd player? ')

rounds = int(input('How many rounds do you want to play: '))
print()

score1 = 0
score2 = 0

operations = ['R', 'P', 'S']

for roundNo in range(1, rounds + 1):
    print(f'Round {roundNo}')
    
    item1 = getInput(player1)
    if playingComputer:
        item2 = operations[randrange(0, len(operations))]
        print(f'The computer played {item2}')
    else:
        item2 = getInput(player2)

    if item1 == item2:
        print('Tie\n')
    elif (operations.index(item1) - operations.index(item2)) % len(operations) == 1:
        print(f'{player1} has won\n')
        score1 += 1
    else:
        print(f'{player2} has won\n')
        score2 += 1

    if abs(score1 - score2) > rounds - roundNo:
        break

if score1 == score2:
    print('The game is a tie')
elif score1 > score2:
    print(f'{player1} has won the game')
else:
    print(f'{player2} has won the game')
