def lastQueenOk(list):
    LQueen = list[-1]
    for j in range(len(list)-1):
        if list[j] == LQueen:
            return False
        if (abs(j-len(list)))/(abs(list[j]-LQueen)) == 1:
            return False
    return True

def isSolution(list):
    while len(list) != 0:
        if lastQueenOk(list) == True:
            list.pop()
            continue
        else:
            return False
    return True

list = [1,2,3,0]
print(isSolution(list))
