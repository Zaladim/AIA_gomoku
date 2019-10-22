from command_gestion import parse
import botkiwi as bk
from classes import Board


def main():
	# print("Kiwi")
	game_gestion = Board()
	try:
		### A supprimer ###
		# test_board = Board()
		# test_board.new(30)
		# test_board.board[14][18] = 2
		# test_board.board[15][15] = 1
		# test_board.board[18][18] = 1
		# test_board.board[13][14] = 1
		# test_board.show()
		# print(bk.IA_decision(test_board))

		while (True):
			cmd = input()
			# print(game_gestion.Board.board)
			# game_gestion.Board = Board(2,2)
			# print(game_gestion.Board.board)
			code = parse(cmd, game_gestion)
			# print(game_gestion.Board.board)
			if (code == 84):
				return 84
			if (code == 1):
				break
			# game_gestion.show()
	except KeyboardInterrupt:
		return 0
	return 0

if __name__ == "__main__":
	main()
