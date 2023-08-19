# Import packages
from sys import stderr
from random import choice

class Bot:
	# Generic class for all bots
	# Contains 2 key functions
	# __init__: Initializes the bot
	# get_move: Takes in the current board state as input and outputs the next move to play

	def __init__(self, time_per_move, color, board):
		# Function that is called when the bot is created
		# All initialization is done here

		self.time_per_move = time_per_move
		self.color = color
		self.board = board
		self.peg_pos = [set(), set()]

		# Initialize red_pegs and blue_pegs
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				self.peg_pos[board[i][j]].add((i, j))

	def get_move(self, board):
		# Function to get the next move played by the bot
		# Intended to be overwritten by subclasses
		# Current implementation returns (-1, -1) i.e. resigns

		self.board = board
		return (-1, -1)

	def is_valid_pos(self, x, y):
		# Returns whether the given position is a valid position that can be used to place a peg
		# A position is valid if it meets the following conditions
		# It is within the bounds of the board ([0, BOARD_SIZE), [0, BOARD_SIZE))

		if x < 0 or x >= BOARD_SIZE:
			return False
		if y < 0 or y >= BOARD_SIZE:
			return False


		return (x, y) not in self.red_pegs and (x, y) not in self.blue_pegs

class RandomBot(Bot):
	# This bot selects a random move from the set of legal moves
	
	def get_move(self, board):
		super(RandomBot, self).get_move(board)

		# Find the list of empty cells
		empty_cells = []
		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if self.board[i][j] == 0:
					empty_cells.append((i, j))
		
		# Return a random empty cell
		return choice(empty_cells)

class MinimaxBot(Bot):
	# This bot uses minimax to select the next move
	# A move is selected from all squares a knights move from the current square
	
	MINIMAX_DEPTH = 3

	def find_possible_moves(self, color):
		possible_moves = set()

		for i in range(BOARD_SIZE):
			for j in range(BOARD_SIZE):
				if self.board[i][j] == self.color:
					# Fina all positions a knights move away from the current position
					next_moves = {(x + i, y + j) for x, y in KNIGHTS_MOVE}
					possible_moves = possible_moves.union(next_moves)
	
	def evaluate_position(board, position):
		# Use a simple heuristic to evaluate the current board position value
		pass

	def minimax(self, added_pegs, color, depth):
		if depth

	def get_move(self, board):
		super(MinimaxBot, self).get_move(board)

		# Get a list of all possible moves from here
		

def select_bot(time_per_move, color, board_state):
	# Select a bot given the time_per_move and color
	# Then initialize the bot
	return RandomBot(time_per_move, CELL_CODE[color], board_state)

def log(*args,**kwargs):
	# Log debug message to stderr
	print(*args, file = stderr, **kwargs)

def parse_board_state(board_state):
	# Convert the string representing the board state into a python 2d list
	board = STARTING_BOARD_STATE.copy()

	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			board[i][j] = CELL_CODE[board_state[i * BOARD_SIZE + j]]
	
	return board

# Constants
BOARD_SIZE = 24

STARTING_BOARD_STATE = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
STARTING_BOARD_STATE[0][0] = -1
STARTING_BOARD_STATE[0][-1] = -1
STARTING_BOARD_STATE[-1][0] = -1
STARTING_BOARD_STATE[-1][-1] = -1

CELL_CODE = {
	'M': -1,
	'R': 0,
	'B': 1,
	'W': 2
}

KNIGHTS_MOVE = [
	[-1, -2],
	[-1, 2],
	[1, -2],
	[1, 2],
	[-2, -1],
	[-2, 1],
	[2, -1],
	[2, 1],
]

if __name__ == '__main__':
	while True:
		# Take input
		inp = input().split()

		if inp[0] == 'begin':
			# Game has started
			# Choose a bot based on time per move and color
			bot = select_bot(float(inp[1]), inp[2], STARTING_BOARD_STATE.copy())
			print('ready')

		elif inp[0] == 'startfrom':
			# Parse the current board state 
			# Choose a bot based on time per move and color
			curr_board = parse_board_state(inp[1])
			bot = select_bot(float(inp[2]), inp[3], curr_board)
			print('ready')

		else:
			# Parse the current board state
			# Then pass the board state to the bot to get the next move
			curr_board = parse_board_state(inp[1])
			move = bot.get_move(curr_board)
			print(move[0] + 1, move[1] + 1)
