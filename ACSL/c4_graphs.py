def neighbors(e_arr, fr):
    result = []
    for index, tos in enumerate(e_arr[fr - 1]):
        if tos == True: result.append(index + 1)

    return result

def move(step, paths, e_arr, visited):
    result = []
    last = paths[-1]
    
    if step == 0: 
        # result += paths
        return paths

    for neighbor in neighbors(e_arr, last):
        if neighbor not in visited:
            if step - 1 == 0:
                result.append(move(step - 1, paths + [neighbor], e_arr, visited | {neighbor}))
            else:
                result += move(step - 1, paths + [neighbor], e_arr, visited | {neighbor})

    return result

def sumPathsOfLengthN(num, edges):
    edges = edges.strip().split(' ')
    points = set()
    for edge in edges:
        for p in edge:
            points.add(int(p))
    # print(points)
    e_arr = [[False] * max(points) for i in range(max(points))]
    for edge in edges:
        fr, to = int(edge[0]) - 1, int(edge[1]) - 1
        e_arr[fr][to] = True
    # print(e_arr)
    # print(neighbors(e_arr, 4))
    # print(move(num, [2], e_arr))
    paths = []
    for point in points:
        paths += move(num, [point], e_arr, {point})
    
    total = 0
    for path in paths:
        num = ''
        for p in path:
            num += str(p)
        total += int(num)
    print(paths)
    return total



num = 3
edges = '12 23 31 34 41'
print(sumPathsOfLengthN(num, edges))
