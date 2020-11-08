def checkRow(table,Sum):
    for row in range(len(table)):
        checkSum = 0
        for column in range(len(table)):
            checkSum += table[row][column]
        if checkSum != 15:
            return False
        return True

def checkCol(table,Sum):
    for column in range(len(table)):
        checkSum = 0
        for row in range(len(table)):
            checkSum += table[row][column]
        if checkSum != 16:
            return False
        return True

def checkDiag1(table,Sum):
    checkSum = 0
    for row in range(len(table)):
        checkSum += table[row][row]
    if checkSum != 15:
        return False
    return True

def checkDiag2(table,Sum):
    for row in range((len(table))-1,1,-1):
        checkSum = 0
        for column in range(len(table)):
            checkSum += table[row][column]
            row -= 1
        if checkSum != 15:
            return False
        return True

        
table = [[2, 9, 4],
         [7, 5, 3],
         [6, 1, 8]]

if checkDiag2(table,15) and checkDiag1(table,15) and checkRow(table,15) and checkCol(table,15)   is True:
    print("Table is a magic square")
else:
    print("The table is not a magic square")
