#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 6: Tables and Matrices
#Task6(1)

matrix = [[1, 2, 3,4], [5, 6,7,8], [9,10,11,12]]
final_matrix = []

def transpose(matrix):
    for i in range(len(matrix[0])):
        new_matrix = []
        for j in range(len(matrix)):
            new_matrix.append(matrix [j][i])
            if j == (len(matrix)-1):
                final_matrix.append(new_matrix)
    return final_matrix

print(transpose(matrix))
