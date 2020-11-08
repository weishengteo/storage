#FIND PERMUTATION

def permutations(a, b):
    first = list(range(a, b))
    last = list(reversed(first))
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1])]
    return res

def lex_suc(perm):
    n = len(perm)
    res = perm[:]
    for i in range(n-2, -1, -1):
        if perm[i] < perm[i+1]:
            break
    for j in range(n-1, i, -1):
        if perm[j] > perm[i]:
            break
    res[i], res[j] = res[j], res[i]
    return res[:i+1] + \
            list(reversed(res[i+1:]))

#FIND CYCLE
def cycle(vertices, graph):
    for i in range(len(vertices)):
        if not graph[vertices[i-1]][vertices[i]]:
            return False
    return True

def brute_force_hamiltonian_cycles(graph):
    perms = permutations(1, len(graph))
    res = []
    for perm in perms:
        walk = [0] + perm
        if cycle(walk, graph):
            res += [walk]
    return res

graph = [[0,1,1,1],[1,0,1,1],[0,1,0,0],[1,1,1,0]]
print(brute_force_hamiltonian_cycles(graph))
