#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 19 April 2019
#Workshop 7
#Task 1

board = [[0,0,1,0],
         [1,0,0,0],
         [0,0,0,1],
         [0,1,0,0]]
diag_check =[]
diag_c = []


def is_solution(board,n):
    nextposr = 0
    nextposc = 0
    direct = (-1,1)

    for i in board:
        if sum(i) != 1:
            return False
                   
    for i in range(len(board)):
        column =[]
        for j in range(len(board)):
            column.append(board[j][i])
        if sum(column) != 1:
            return False

    for i in range(len(board)):
        diag_check = []
        for j in range(len(board)):
            if board[i][j] == 1:
                diag_check.append(i)
                diag_check.append(j)        
        diag_c.append(diag_check)

    for i in diag_c:   
        for j in range(1,n+1):
            for dr in direct:
                for dc in direct:
                    nextposr = i[0] + (dr*j)
                    nextposc = i[1] + (dc*j)
                    if nextposc >= 0 and nextposc < 4 and nextposr >= 0 and nextposr < 4: 
                        if board[nextposr][nextposc] == 1:
                            return False
    return True




    
                
    
        

    

    
