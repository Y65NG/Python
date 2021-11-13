from pprint import pprint

graph = 'XA 5 AG 1 GX 6 AM 9 MA 6 MG 4 ZM 3 GZ 2'
total_weights = [0]
def dfs(table, visited, start, now, total):
    
    global total_weights
    points = ['A', 'G', 'M', 'X', 'Z']
    for to, w in enumerate(table[now]):
        temp = set(list((visited)))
        if w != 0:
            print(visited)
            print('to:', points[to])
            print(w, start)
            if to == start:
                total_weights.append(total + w)
                print('total:', total + w)
                return
                # return total
            elif to not in visited:
                temp.add(to)
                
                dfs(table, temp, start, to, total + w)
    return
    # total_weights.append(total)
    # return total

def find_max_weight(graph):
    graph = graph.strip().split(' ')
    d_graph = []
    points = set()
    weights = {}
    print(graph)
    for i in range(len(graph)):
        e = graph[i]
        if i % 2 == 0: # edge
            # print(i)
            for p in e: points.add(p)
        else:
            w = int(e)
            weights[graph[i-1]] = w

    points = list(points)
    points.sort()
    print(points)
    print(weights)
    table = [[0] * (len(points)) for i in range(len(points))]
    # print(table)

    for e in weights:
        p1, p2 = e[0], e[1]
        table[points.index(p1)][points.index(p2)] = weights[e]
    # pprint(table)

    for p in points:
        print(p)
        dfs(table, set(), points.index(p), points.index(p), 0)
    return max(total_weights)
    

print(find_max_weight(graph))
print(total_weights)