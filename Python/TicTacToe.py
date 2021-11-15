from tkinter import *
import tkinter.messagebox as mb

movesleft = 0

def play(x, y):
    if board[y][x] == 0:
        global move, movesleft, mode
        board[y][x] = move
        buttons[y][x]['text'] = text[move]
        move = move % 2 + 1
        movesleft -= 1
        if not check() and mode and move == 2: chooseMove()
    else:
        mb.showerror('Error', 'This move is not valid. Please choose another square.')

def check():
    for y in range(3):
        if board[y][0] != 0 and board[y][1] == board[y][0] and board[y][2] == board[y][0]:
            win()
            return True
    for x in range(3):
        if board[0][x] != 0 and board[1][x] == board[0][x] and board[2][x] == board[0][x]:
            win()
            return True
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        win()
        return True
    if board[0][2] != 0 and board[0][2] == board[1][1] and board[2][0] == board[1][1]:
        win()
        return True
    if movesleft == 0:
        popupmsg("It is a tie")
        return True
    return False

def win(): popupmsg("The winner is " + text[move % 2 + 1])

def popupmsg(msg):
    MsgBox = mb.askquestion ('Game Over', msg + '\nDo you want to play again?')
    if MsgBox == 'no': game.destroy()
    else:
        global board, text, buttons, movesleft, mode, move
        movesleft = 9
        move = 1
        board = [[0] * 3 for _ in range(3)]
        text = {0: '', 1: 'X', 2: 'O'}
        for y in buttons:
            for button in y:
                button['text'] = ''

def getState():
    res = False, [], False
    for c in checkConfigs:
        t = [board[i[1]][i[0]] for i in c]
        if t.count(2) == 2:
            for i in range(3):
                if t[i] == 0: return True, c[i][0], c[i][1]
        if t.count(1) == 2:
            for i in range(3):
                if t[i] == 0: res = True, c[i][0], c[i][1]
    return res

def chooseMove():
    print(board)
    for b in range(len(sp)):
        if board == sp[b]:
            play(spmoves[b][0], spmoves[b][1])
            return
    k = getState()
    if k[0]:
        play(k[1], k[2])
        return
    for y in (0, 2):
        for x in (0, 2):
            if board[y][x] == 0:
                play(x, y)
                return
    for y, x in ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)):
        if board[y][x] == 0:
            play(x, y)
            return

def func00(): play(0, 0)
def func01(): play(0, 1)
def func02(): play(0, 2)
def func10(): play(1, 0)
def func11(): play(1, 1)
def func12(): play(1, 2)
def func20(): play(2, 0)
def func21(): play(2, 1)
def func22(): play(2, 2)

game = Tk()
game.title("Tic Tac Toe")

w = 40
h = 12

mode = False

move = 1
movesleft = 9
checkConfigs = [[[i, j] for j in range(3)] for i in range(3)] + [[[i, i] for i in range(3)]] + [[[i, 2 - i] for i in range(3)]] + [[[j, i] for j in range(3)] for i in range(3)]
sp = [[[2, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [0, 0, 0]], [[0, 0, 1], [0, 2, 0], [1, 0, 0]], [[0, 0, 0], [0, 0, 0], [1, 0, 0]]]
spmoves = [[1, 1], [1, 1], [0, 1], [0, 1]]

board = [[0] * 3 for _ in range(3)]
text = {0: '', 1: 'X', 2: 'O'}

buttonFuncs = [[func00, func01, func02], [func10, func11, func12], [func20, func21, func22]]
buttons = [[] for i in range(3)]
for y in range(3):
    for x in range(3):
        button = Button(game, width = w, height = h, command = buttonFuncs[x][y])
        button.grid(row = y, column = x)
        buttons[y].append(button)

mode = mb.askquestion ('Select Mode', 'Do you want to play against the computer?') == 'yes'

game.mainloop()
