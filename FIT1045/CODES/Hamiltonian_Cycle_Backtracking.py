def solutions(completed, options, partial=[]):
    if completed(partial):
        return [[0] + partial]
    else:
        res = []
        for o in options(partial):
            augmented = partial+[o]
            #print(o,augmented)
            res += solutions(completed, options, augmented)
        return res

def hamiltonian_cycles(graph):
    def completed(partial):
        '''if partial != []:
            print (partial, partial[-1],graph[partial[-1]][0])'''
        return len(partial)+1 == len(graph) and graph[partial[-1]][0]

    def neighbours(path, graph):
        neigh = []
        for j in range(len(graph)):
                if graph[path][j] == 1:
                    neigh += [j]
        return neigh

    def options(partial):
        res = []
        path = [0] + partial
        for v in neighbours(path[-1], graph):
            if v not in path:
                res += [v]
        return res

    return solutions(completed, options)

graph = [[0,1,1,1],[1,0,1,1],[0,1,0,0],[1,1,1,0]]
print(hamiltonian_cycles(graph))
