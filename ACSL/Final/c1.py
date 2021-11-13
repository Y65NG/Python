pieces = 'Rc1 Kd8 Qb6 Re5 Bh3'

def convert(piece):
    return (piece[0], ord(piece[1]) - 97, int(piece[2]) - 1)

def init(piecees):
    result = {}
    for piece in piecees:
        if piece[0] not in result:
            result[piece[0]] = [(piece[1], piece[2])]
        else: result[piece[0]].append((piece[1], piece[2]))
    return result

def line_move(white_poses, pos):
    result = set()
    p_x, p_y = pos
    for x in range(p_x-1, -1, -1):
        if (x, p_y) not in white_poses: result.add((x, p_y))
        else: break
    for x in range(p_x+1, 8):
        if (x, p_y) not in white_poses: result.add((x, p_y))
        else: break
    for y in range(p_y-1, -1, -1):
        if (p_x, y) not in white_poses: result.add((p_x, y))
        else: break
    for y in range(p_y+1, 8):
        if (p_x, y) not in white_poses: result.add((p_x, y))
        else: break
    return result

def diag_move(white_poses, pos):
    result = set()
    p_x, p_y = pos

    index = 1
    for x in range(p_x-1, -1, -1):
        y = p_y - index
        if y == -1: break
        if (x, y) not in white_poses: result.add((x, y))
        else: break
        index += 1

    index = 1
    for x in range(p_x+1, 8):
        y = p_y + index
        if y == 8: break
        if (x, y) not in white_poses: result.add((x, y))
        else: break
        index += 1

    index = 1
    for x in range(p_x-1, -1, -1):
        y = p_y + index
        if y == 8: break
        if (x, y) not in white_poses: result.add((x, y))
        else: break
        index += 1
    
    index = 1
    for x in range(p_x+1, 8):
        y = p_y - index
        if y == -1: break
        if (x, y) not in white_poses: result.add((x, y))
        else: break
        index += 1
    return result

def p_move(white_poses, pos):
    if pos[1] != 8: return {(pos[0], pos[1] + 1)}
    return {pos}

def n_move(white_poses, pos):
    x, y = pos
    result = {(x-1, y+2), (x+1, y+2), (x-2, y+1), (x+2, y+1), (x-2, y-1), (x+2, y-1), (x-1, y-2), (x+1, y-2)}
    for i in result:
        if i in white_poses: result.remove(i)
    return result

def k_move(pos):
    x, y = pos
    result = {(x-1, y+1), (x, y+1), (x+1, y+1), 
            (x-1, y),             (x+1, y), 
            (x-1, y-1), (x, y-1), (x+1, y-1)}

    if x == 0: 
        result.remove((x-1, y+1))
        result.remove((x-1, y))
        result.remove((x-1, y-1))
    if x == 7:
        result.remove((x+1, y+1))
        result.remove((x+1, y))
        result.remove((x+1, y-1))
    if y == 0:
        result.remove((x-1, y-1))
        result.remove((x, y-1))
        result.remove((x+1, y-1))
    if y == 7:
        result.remove((x-1, y+1))
        result.remove((x, y+1))
        result.remove((x+1, y+1))
    return result

def occupy(board, poses, piece, pos):
    white_poses = set()
    for x in poses:
        if x != 'K':
            for p in poses[x]:
                if p != pos: white_poses.add(p)
    
    
    if piece == 'Q':
        # print('Q')
        for i in line_move(white_poses, pos): board[i[0]][i[1]] = True
        for i in diag_move(white_poses, pos): board[i[0]][i[1]] = True
    elif piece == 'R':
        # print('R')
        for i in line_move(white_poses, pos): 
            # print(i)
            board[i[0]][i[1]] = True
    elif piece == 'B':
        # print('B')
        for i in diag_move(white_poses, pos): board[i[0]][i[1]] = True
    elif piece == 'P':
        # print('P')
        for i in p_move(white_poses, pos): board[i[0]][i[1]] = True
    elif piece == 'N':
        # print('N')
        for i in n_move(white_poses, pos): board[i[0]][i[1]] = True
       

def find_king_status(pieces):
    pieces = [convert(x) for x in pieces.strip().split(' ')]
    poses = init(pieces)
    # print(poses)
    board = [[False] * 8 for i in range(8)]
    # print(board)

    K = poses['K'][0]

    for piece in poses:
        for pos in poses[piece]:
            # print(pos)
            occupy(board, poses, piece, pos)
    # print(board)

    x, y = K
    if not board[x][y]:
        status = True
        for i in k_move(K):
            if not board[i[0]][i[1]]: status = False
        if status: return 'STALEMATE'
        else: return 'SAFE'
    else:
        status = True
        for i in k_move(K):
            print(i)
            if not board[i[0]][i[1]]: status = False
        if status: return 'CHECKMATE'
        else: return 'CHECK'



print(find_king_status(pieces))
    