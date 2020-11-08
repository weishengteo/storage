#Spanning Tree

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
        found = False
        for i in conn:
            for j in range(n):
                if j not in conn and graph[i][j]==1:
                    tree[i][j] = 1
                    tree[j][i] = 1
                    conn = conn + [j]
                    found = True
                    break
            if found:
                break
    return tree

G = [[0,1,1,1],
     [1,0,1,1],
     [1,1,0,0],
     [1,1,0,0]]
print(spanning_tree(G))
