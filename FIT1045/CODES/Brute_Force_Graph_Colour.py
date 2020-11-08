#Possible minimising graph colour problem using Brute Force? 

def permutation(n):
    #Fix this! Generate combination!
    perm = [[0,0,0],[0,0,1],[0,1,0],[1,0,0],[0,1,2]]
    return perm

def valid_states(adj_mat,p):
    for i in range(len(p)):
        for j in range(i+1,len(p)):
            if adj_mat[i][j] == 1 and p[i] == p[j]:
                return False
    return True
           
def colours(p):
    col_list = []
    for colour in p:
        if colour not in col_list:
            col_list.append(colour)
    number = len(col_list)
    return number

adj_mat = [[0,1,1],[1,0,0],[1,0,0]]
n = len(adj_mat)
perm = permutation(n)
opt = list(range(n))

for p in perm:
    print(valid_states(adj_mat,p),p)
    if valid_states(adj_mat,p):
        if colours(p) < colours(opt):
            opt = p
            
print(opt,colours(opt))
            
