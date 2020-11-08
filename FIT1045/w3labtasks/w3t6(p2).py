#Name = Teo Wei Sheng
#Date = 22 March 2019
#Task 6: Tables and matrices
#Task6(2)
       
def vmmultiply(v, m):
    newv = []
    for i in range(len(m)):
        total = 0
        for j in range(len(v)):
            total += m[i][j] * v[j]
            if j == (len(v) - 1):
                newv.append(total)
    return newv

print(vmmultiply([1,2,3,4],[[1,2,3,3],[4,5,6,6],[7,8,9,9],[10,11,12,13]]))
