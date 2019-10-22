import parser

def evaluate(board, length, height):
	eval = []
	for i in range(height):
		row = []
		for j in range(length):
			row.append(0)
		eval.append(row)

def is_blocked(board, y, x, height, length) :
    if (y < 0 or y > height - 1) :
        return 1
    if (x < 0 or x > length - 1):
        return 1
    if (board[y][x] == 2):
        return 1
    return 0


def fill_wmatrice(board, weight_matrice, y, x, height, length) :
    winning_size = 5
    boost = 1

    weight_matrice[y][x] = 0
    for k in range(y + 1, y + winning_size) :
        if is_blocked(board, k, x, height, length):
            break
        if board[k][x] == 1:
            boost += 1
        else:
            weight_matrice[k][x] += boost
    boost = 1
    for k in range(y - 1, y - winning_size, - 1):
        if is_blocked(board, k, x, height, length):
            break
        if board[k][x] == 1:
            boost += 1
        else:
            weight_matrice[k][x] += boost
    boost = 1
    for k in range(x + 1, x + winning_size) :
        if is_blocked(board, y, k, height, length):
            break
        if board[y][k] == 1:
            boost += 1
        else:
            weight_matrice[y][k] += boost
    boost = 1
    for k in range(x - 1, x - winning_size, -1):
        if is_blocked(board, y, k, height, length):
            break
        if board[y][k] == 1:
            boost += 1
        else:
            weight_matrice[y][k] += boost
    boost = 1
    for k in range(1, winning_size) :
        if is_blocked(board, y + k, x - k, height, length):
            break
        if board[y + k][x - k] == 1:
            boost += 1
        else:
            weight_matrice[y + k][x - k] += boost
    boost = 1
    for k in range(1, winning_size):
        if is_blocked(board, y + k, x + k, height, length):
            break
        if board[y + k][x + k] == 1:
            boost += 1
        else:
            weight_matrice[y + k][x + k] += boost
    boost = 1
    for k in range(1, winning_size):
        if is_blocked(board, y - k, x + k, height, length):
            break
        if board[y - k][x + k] == 1:
            boost += 1
        else:
            weight_matrice[y - k][x + k] += boost
    boost = 1
    for k in range(1, winning_size):
        if is_blocked(board, y - k, x - k, height, length):
            break
        if board[y - k][x - k] == 1:
            boost += 1
        else:
            weight_matrice[y - k][x - k] += boost

def check_prox(board, height, length, coord):
    if (coord[0] > 0):
        if (coord[1] > 0 and board[coord[0] - 1][coord[1] - 1] > 0):
            return 0
        if (coord[1] < length - 1 and board[coord[0] - 1][coord[1] + 1] > 0):
            return 0
        if (board[coord[0] - 1][coord[1]] > 0):
            return 0
    if (coord[0] < height - 1):
        if (board[coord[0] + 1][coord[1]] > 0):
            return 0
        if (coord[1] > 0 and board[coord[0] + 1][coord[1] - 1] > 0):
            return 0
        if (coord[1] < length - 1 and board[coord[0] + 1][coord[1] + 1] > 0):
            return 0
    if (coord[1] > 0 and board[coord[0]][coord[1] - 1] > 0):
        return 0
    if (coord[0] > 0 and coord[1] < height - 2 and board[coord[0] - 1][coord[1] + 1] > 0):
        return 0
    return 1
    

def IA_decision(board, height, length):
    #construit la matrice de poid à enlever si on veut la concerver d'une étape à l'autre.
    weight_matrice = []
    for i in range(length) :
        row = []
        for j in range(height) :
            row.append(0)
        weight_matrice.append(row)
    #rempli la matrice de poids
    for i in range(height) :
        for j in range(length) :
            #si je trouve un pion à moi, je rempli ma matrice de poid.
            if (board[i][j] == 1) :
                fill_wmatrice(board, weight_matrice, i, j, height, length)
    #cherche les coordonnées de la case la plus forte:
    best_value = 0
    best_coord = [0, 0]
    
    #MININMAX
    best_coord = minimax(weight_matrice, board, height, length)
    #MINIMAX END

    #NON MINIMAX
    # for i in range(height) :
    #     for j in range(length) :
    #         if (weight_matrice[i][j] > best_value and not check_prox(board, height, length, (i, j))):
    #             best_value = weight_matrice[i][j]
    #             best_coord = [i, j]

    #pour l'exemple: l'algorythme doit nous renvoyer 14, 14
    #print("Best value: %d" % best_value)
    #print("Affichage de la matrice de poid:")
    #for row in weight_matrice:
	#    print(row)
    
    return (best_coord)

def minimax(weight, board, height, length):
    coord = []
    for i in range(len(weight)):
        for j in range(len(weight[0])):
            if (weight[i][j] > 0 and not check_prox(board, height, length, (i, j))):
                coord.append([i, j, weight[i][j]])
    best_coord = minimax_alg(coord, True)
    return ([best_coord[0], best_coord[1]])
    
def minimax_alg(coord, player):
    if (len(coord) == 1):
        return coord[0]
    chunk = chunks(coord, 3)

    new = []
    if player:
        for item in chunk:
            point = [0, 0, 0]
            for i in range(len(item)):
                if (item[i][-1] > point[-1]):
                    point = item[i]
            new.append(point)
        return minimax_alg(new, False)
    else:
        for item in chunk:
            point = item[0]
            for i in range(1, len(item)):
                if (item[i][-1] < point[-1]):
                    point = item[i]
            new.append(point)
        return minimax_alg(new, True)


def chunks(list, n):
    n = max(1, n)
    return (list[i:i+n] for i in range(0, len(list), n))