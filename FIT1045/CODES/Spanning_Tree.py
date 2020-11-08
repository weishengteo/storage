#Spanning Tree
def extension(vertices, graph):
    n = len(graph)
    for i in vertices:
        for j in range(n):
            if j not in vertices and graph[i][j]:
                return i, j

def spanning_tree(graph):
    '''input: graph given as adjacency matrix
       output: spanning tree of graph (as adj. mat)'''
    n = len(graph)
    tree =  [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    conn = [0]
    while len(conn) < n:
        i, j = extension(conn, graph)
        tree[i][j] = 1
        tree[j][i] = 1
        conn = conn + [j]
    return tree

G = [[0,1,1,1],
     [1,0,1,1],
     [1,1,0,0],
     [1,1,0,0]]

print(spanning_tree(G))

