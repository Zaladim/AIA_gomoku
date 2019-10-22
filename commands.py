
from classes import Board
import gomoku as gmk

def start(size):
	gmk.game_gestion.new(size, size)
	gmk.game_gestion.show()
	return 0

def turn(x, y):
	gmk.game_gestion.Board.play(x, y, 2)
	return ([0, 0])
	#L'ia réfléchit:
	#return la réponse

def begin():
	return
	#L'ia réfléchit:
	#gmk.game_gestion.Board.play(data[0], data[1], 2)
	#return la réponse

def about():
	gmk.game_gestion.Board.about()

# def board(data) :
# 	gmk.game_gestion.Board =
