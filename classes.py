from random import randint
import botkiwi

class Board:
	#On dit qu'on est les blanc tout le temps!
	COLOR = {
		"NOTHING":0,
		"WHITE":1,
		"BLACK":2,
	}

	def __init__(self):
		self.board = []
		self.length = 0
		self.height = 0

		self.name = "\"PM_bot\""
		self.version = "\"1.0\""
		self.author = "\"Paul et Martin\""
		self.country = "\"France\""

		self.timeout_turn = 0
		self.timeout_match = 0
		self.max_memory = 0
		self.time_left = 0
		self.game_type = 0
		self.rule = 0
		self.evaluate = (0, 0)
		self.folder = "."

	def new(self, size):
		self.board = []
		for i in range(size) :
			row = []
			for j in range(size):
				row.append(0)
			self.board.append(row)
		self.length = size
		self.height = size
		return self

	def turn(self, x, y, last_color) :
		self.play(x, y, last_color)
		move = self.give_best_move()
		self.play(move[0], move[1], 1)
		return (move[0], move[1])

	def play(self, x, y, color):
		if (x < self.length and y < self.height and x >= 0 and y >= 0):
			self.board[x][y] = color
		else:
			return 84

	def give_best_move(self):
		# TEST BOT
		weight = botkiwi.IA_decision(self.board, self.height, self.length)
		# END TEST BOT
		# x = randint(0, self.height - 1)
		# y = randint(0, self.length - 1)
		return weight

	def begin(self):
		x = randint(0, self.length - 1)
		y = randint(0, self.height - 1)

		self.board[x][y] = 1

		return x, y

	def f_board(self, turns):
		for turn in turns[:-1] :
			self.play(int(turn[0]), int(turn[1]), int(turn[2]))
		turn = turns[-1]
		return(self.turn(int(turn[0]), int(turn[1]), int(turn[2])))
	
	def info(self, key, value):
		if (key == "timeout_turn"):
			self.timeout_turn = value
		elif (key == "timeout_match"):
			self.timeout_match = value
		elif (key == "max_memory"):
			self.max_memory = value
		elif (key == "time_left"):
			self.time_left = value
		elif (key == "game_type"):
			self.game_type = value
		elif (key == "rule"):
			self.rule = value
		elif (key == "evaluate"):
			self.evaluate = value
		elif (key == "folder"):
			self.folder = value
		return 0
		

	def about(self):
		print("name=" + self.name + ", version=" + self.version + ", author=" + self.author + ", country=" + self.country)

	def show(self):
		for line in self.board:
			print(line)

