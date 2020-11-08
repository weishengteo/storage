from math import inf

def neighbours(path, graph):
        neigh = []
        for j in range(len(graph)):
                if graph[path][j]:
                    neigh += [j]
        return neigh

def dfs_traversal(graph, s):
    visited = []
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop()
        visited += [v]
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
    return visited

def bfs_distances(graph, s):    
    visited = []
    boundary = [s]
    while len(boundary) > 0:
        v = boundary.pop(0)
        visited += [v]
        for w in neighbours(v, graph):
            if w not in visited and w not in boundary:
                boundary.append(w)
    return visited

graph = [[0,1,1,1],[1,0,1,1],[0,1,0,0],[1,1,1,0]]
print(dfs_traversal(graph, 0))
print(bfs_distances(graph, 0))
