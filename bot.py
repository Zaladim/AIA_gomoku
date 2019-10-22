patterns = {
	"11111":1000,
	"11110":100,
	"11101":100,
	"11011":100,
	"11100":10,
	"10101":10,
	"10011":10,
	"11000":1,
	"10001":1,
	"01100":1
}

def evaluate(board, length, height):
	eval = []
	for i in range(height) :
		row = []
		for j in range(length):
			row.append(0)
		eval.append(row)


def pattern_rec(board, length, height, pos):
	pattern = board[pos[0]]
	pattern[pos[1]] = 1
	pattern = pattern[max(0, pos[1]-4):min(pos[1]+5, length)]

	pattern[0] = 1
	pattern[1] = 1
	# pattern[5] = 2
	print(pattern)
	val = eval_pattern(pattern)
	print(val)
	return 0

def get_diag(board, length, height, pos):
	board[pos[0]][pos[1]] = 1
	x = max(pos[0]-4, height)
	y = max(pos[1]-4, length)
	pattern = []
	try:
		while(len(pattern) < 9 and x < height and y < length):
			pattern.append(board[x][y])
			x += 1
			y += 1

def eval_pattern(pattern):
	val = 0
	for i in range(len(pattern) - 5):
		tmp = 0.5
		if (2 in pattern[i:i+5]):
			continue
		for elem in pattern[i:i+5]:
			if (elem == 1):
				tmp *= 2
		print(tmp)
		val += tmp
	return val
