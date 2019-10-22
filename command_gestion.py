from classes import Board

def parse(cmd, game_gestion):
	data = cmd.split()
	try:
		return CMD[data[0]](data[1:], game_gestion)
	except KeyError:
		return 0

def start(data, game_gestion):
	try:
		if (len(data) != 1):
			print("ERROR message - unsupported size")
			return 84
		size = int(data[0])
		if (size < 2):
			print("ERROR message - unsupported size")
			return 84

		# commands.start(size)
		game_gestion.new(size)

	except ValueError:
		print("ERROR message - invalid data Test")
		return 84

	print("OK")
	return 0

def turn(data, game_gestion):
	try:
		if (len(data) != 1):
			print("ERROR message - invalid command")
			return 84
		coor = data[0].split(',')
		y = int(coor[0])
		x = int(coor[1])

		coor = game_gestion.turn(x, y, 2)
		print(str(coor[1]) + "," + str(coor[0]))

	except (ValueError, IndexError):
		print("ERROR message - invalid data test2")
		return 84
	return 0

def begin(data, game_gestion):
	try:
		if (len(data) != 0):
			print("ERROR message - invalid command")
			return 84

		x, y = game_gestion.begin()

		print(str(y) + "," + str(x))

	except (ValueError, IndexError):
		print("ERROR message - invalid data kiwi ")
		return 84
	return 0

def board(data, game_gestion):
	turns = []
	line = input()
	while (line != "DONE"):
		turns.append(line.split(','))
		line = input()
	print(game_gestion.f_board(turns))
	return 0

def info(data, game_gestion):
	try:
		if (len(data) != 2):
			print("ERROR message - invalid command")
			return 84
		key = data[0]
		value = data[1]

	except ValueError:
		print("ERROR message - invalid data info")
		return 84
	return 0

def end(data, game_gestion):
	return 1

def about(data, game_gestion):
	game_gestion.about()
	return 0

CMD = {
	"START":start,
	"TURN":turn,
	"BEGIN":begin,
	"BOARD":board,
	"INFO":info,
	"END":end,
	"ABOUT":about
}
