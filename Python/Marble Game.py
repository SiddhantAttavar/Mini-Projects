# Nine marbles are kept on a rock and numbered 1 through 9. On each turn, a player
# takes one of the marbles off of the rock and keeps it. The first one who can make
# exactly three of their marbles add up to 15 is the winner. If Simba goes first, and both
# play optimally, who will win?

def checkWin(marbles):
    possibleSums = {0}
    for marble in marbles:
        possibleSums = possibleSums.union(set([marble + x for x in possibleSums]))
        if finalSum in possibleSums:
            return True
    return False

def gameState(marbles):
    playerA = []
    playerB = []

    for marble, player in enumerate(marbles):
        if player == 0:
            playerA.append(marble + 1)
        else:
            playerB.append(marble + 1)
    
    if checkWin(playerA):
        return 1
    if checkWin(playerB):
        return -1
    return 0

def solve(marbles, turn, depth):
    if depth == len(marbles):
        # We have reached the end of the game
        return gameState(marbles)
    
    # Maximize score
    res = -2
    for marble, player in enumerate(marbles):
        if player == -1:
            # We can take this marble
            nextMarbles = marbles.copy()
            nextMarbles[marble] = 1
            res = max(res, -solve(nextMarbles, (turn + 1) % 2, depth + 1))
    
    return res

numMarbles = 9
finalSum = 15
res = solve([-1] *  numMarbles, 0, 0)
if res == -1:
    print('Lose')
elif res == 0:
    print('Draw')
else:
    print('Win')