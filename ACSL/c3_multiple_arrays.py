from pprint import pprint


def move(pos, row, col):
    x, y = pos
    result = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1),             (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
    ]
    # print(result)
    if x == 0: 
        i = 0
        while i < len(result):
            if result[i][0] == x - 1: 
                result.remove(result[i])
                i -= 1
            i += 1

    if x == row - 1: 
        i = 0
        while i < len(result):
            if result[i][0] == x + 1: 
                result.remove(result[i])
                i -= 1
            i += 1

    if y == 0:
        i = 0
        while i < len(result):
            if result[i][1] == y - 1: 
                result.remove(result[i])
                i -= 1
            i += 1

    if y == col - 1:
        i = 0
        while i < len(result):
            if result[i][1] == y + 1: 
                result.remove(result[i])
                i -= 1
            i += 1

    # print(result)
    return result

def sumOfMinAlongPath(dim, arrays):
    row, col = [int(x) for x in dim.split(' ')]
    arrs = []
    for string in arrays:
        tmp = string.strip().split(' ')
        arr = [[] for i in range(row)]
        # print(arr)
        # print(tmp)
        index = 0
        for i, num in enumerate(tmp):
            arr[index].append(int(num))
            if i % col == col - 1: index += 1
        arrs.append(arr)
    # for arr in arrs: pprint(arr, width=15)

    visited = set()
    cur_pos = (0, 0)
    min_sum = 0
    visited.add(cur_pos)

    while True:
        neighbors = []
        poses = {}

        for pos in move(cur_pos, row, col):
            x, y = pos
            for arr in arrs:
                neighbors.append(arr[x][y])
                poses[arr[x][y]] = (x, y)
        
        max_num = -99999

        # print('cur_pos:', cur_pos)
        # print(neighbors)

        for num in neighbors:
            tmp = neighbors[:]
            tmp.remove(num)
            if num not in tmp and num > max_num: max_num = num
        
        path_nums = set()
        for arr in arrs:
            path_nums.add(arr[cur_pos[0]][cur_pos[1]])
        min_num = min(path_nums)
        min_sum += min_num
        cur_pos = poses[max_num]
        if cur_pos not in visited: visited.add(cur_pos)
        else: break
    print(min_sum)
    return min_sum




sumOfMinAlongPath('4 5', ['-2 -1 -4 -1 -5 -9 -2 -6 -5 -3 -5 -4 -9 -7 -9 -3 -2 -3 -8 -4', '-6 -2 -6 -4 -3 -3 -8 -3 -2 -7 -1 -2 -4 -8 -4 -2 -1 -1 -3 -9', '-2 -4 -6 -8 -6 -5 -2 -3 -3 -5 -7 -9 -7 -5 -3 -5 -2 -3 -5 -7', '-4 -5 -2 -6 -9 -1 -3 -6 -8 -9 -1 -2 -5 -6 -2 -9 -6 -5 -3 -2', '-3 -1 -4 -1 -5 -9 -2 -6 -5 -3 -5 -8 -9 -7 -9 -3 -2 -3 -8 -4', '-6 -2 -6 -4 -3 -3 -8 -3 -2 -7 -3 -1 -8 -1 -5 -9 -2 -6 -5 -3', '-5 -8 -9 -7 -9 -3 -2 -3 -8 -4 -6 -2 -6 -4 -3 -3 -8 -3 -2 -7'])

# sumOfMinAlongPath('4 4', ['5 2 8 3 1 8 5 3 0 7 1 7 9 5 8 6', '5 4 0 9 5 4 6 2 8 1 8 2 8 1 7 2', '2 7 1 8 2 8 5 8 2 8 4 5 9 0 4 5']) 

