#Name = Teo Wei Sheng
#Student id = 29800668
#Date = 2 April 2019
#Assignment 1
#Task 2: Reversi

#1 = black
#2 = white
#0 = nothing

import copy

def new_board():
    board = []
    for x in range(8):
        board.append([" "," "," "," "," "," "," "," "])
        for y in range(8):
            board[x][y] = 0
    
    board[3][3] = 2
    board[4][3] = 1
    board[3][4] = 1
    board[4][4] = 2

    return board

def score(board):
    s1 = 0
    s2 = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 1:
                s1 += 1
            elif board[x][y] == 2:
                s2 += 1

    return (s1, s2)
                    

def print_board(board):
    hline = "   +---+---+---+---+---+---+---+---+"
    vline = "   |   |   |   |   |   |   |   |   |"
    alph = "abcdefgh"
    alph_list = list(alph)
    print(hline)
    for x in range(8):
        print(vline)
        print (x + 1, end = " ")
        for y in range(8):
            print(" | %s" %(board[x][y]), end = "")
        print (" |")
        print(vline)
        print(hline)
    for i in alph_list:
        if i == "a":
            print("   | ", end = "")
            print (i, end = " | ")
        else:
            print (i, end = " | ")
    


def enclosing(board, player, pos, direct):
    (r, c) = pos
    (dr, dc) = direct
    if player == 1:
        for i in range(1,8):
            if r < 8 and c < 8 and r >= 0 and c >= 0:
                nextposr = (r + dr*i)
                nextposc = (c + dc*i)
                if nextposr > 7 or nextposc > 7 or (i == 1 and board[nextposr][nextposc] == 1):
                    return False
                elif board[nextposr][nextposc] == 1:
                    return True
                elif board[nextposr][nextposc] == 2:
                    continue
                else:
                    return False        
    elif player == 2:
        for i in range(1,8):
            if r < 8 and c < 8 and r >= 0 and c >= 0:
                nextposr = (r + dr*i)
                nextposc = (c + dc*i)
                if nextposr > 7 or nextposc > 7 or (i == 1 and board[nextposr][nextposc] == 2):
                    return False
                elif board[nextposr][nextposc] == 2:
                    return True
                elif board[nextposr][nextposc] == 1:
                    continue
                else:
                    return False


def valid_moves(board, player):
    validmoves = []
    direct = (-1,0,1)
    
    for r in range(8):
        for c in range(8):
            if board[r][c] == 0:
                for dr in direct:
                    for dc in direct:
                        if enclosing(board,player,(r,c),(dr,dc)) == True :
                            validmoves.append((r,c))
                            continue
    return validmoves


def next_state(board, player, pos):

    next_player = 0
    direct = (-1, 0, 1)
    (r,c) = pos

    if player == 1:
        moves = valid_moves(board,player)

        if pos not in moves:
            print("That is an invalid move")

        if pos in moves:
            board[r][c] = 1
            for dr in direct:
                for dc in direct:
                    while enclosing(board,1,(r,c),(dr,dc)) == True:
                        for i in range(1,8):
                            if (r+dr*i) < 7 and (r+dr*i) > 0 and (c+dc*i) < 7 and (c+dc*i) > 0:
                                if board[r + dr*i][c + dc*i] == 2:
                                    board[r + dr*i][c + dc*i] = 1
                                elif board[r + dr*i][c + dc*i] == 1 or 0:
                                    break
                        else:
                            continue
   
        next_player = 2
        return(board, next_player)

    if player == 2:
        moves = valid_moves(board,player)

        if pos not in moves:
            print("That is an invalid move")

        if pos in moves:
            board[r][c] = 2
            for dr in direct:
                for dc in direct:
                    while enclosing(board,2,(r,c),(dr,dc)) == True:
                        for i in range(1,8):
                            if (r+dr*i) < 7 and (r+dr*i) > 0 and (c+dc*i) < 7 and (c+dc*i) > 0:
                                if board[r + dr*i][c + dc*i] == 1:
                                    board[r + dr*i][c + dc*i] = 2
                                    continue
                                elif board[r + dr*i][c + dc*i] == 2 or 0:
                                    break
                            else:
                                continue
        next_player = 1
        return (board, next_player)

def position(string):
    column, row = string[0], (int(string[1])-1)

    alphabet = ["a","b","c","d","e","f","g","h"]
    num = [0,1,2,3,4,5,6,7]

    for i in range(8):
        if column == alphabet[i]:
            column = num[i]
            return row, column
        
    if string[0] not in alphabet or string[1] not in num:
        return None


def run_two_players():
    board = new_board()
    validp1 = valid_moves(board,1)
    validp2 = valid_moves(board,2)

    while len(validp1) > 0 and len(validp2) > 0:
        player = int(input("Which player's turn is it to drop a stone?"))
        
        if player == "q":
            quit()
        else:
            print_board(board)
            print("\nIt is player",player,"'s turn to drop a stone")
            
        string = (input("Where would you like to place your stone?"))

        move = position(string)

        validp1 = valid_moves(board,1)
        validp2 = valid_moves(board,2)

        if player == 1:
            if move in validp1:
                next_state(board, player, move)
            elif move not in validp1:
                print("Invalid move")
                
        if player == 2:
            if move in validp2:
                next_state(board, player, move)
            elif move not in validp2:
                print("Invalid move")

        if len(validp1) < 0 and len(validp2) < 0:
            (s1, s2) = score(board)
            if s1> s2:
                print("Congratuations, player 1, you have beaten player 2!")
                break
            elif s2 > s1:
                print("Congratulations, player 2, you have beaten player 1!")
                break

def comp_best_move(board,player):
    valid = list(valid_moves(board,2))
    countlist = []
    for validm in valid:
        
        bcopy = copy.deepcopy(board)
        xboard = (next_state(bcopy, player, validm)[0])
        count = 0
        
        for i in range(len(xboard)):
            for j in range(len(xboard[0])):
                if xboard[i][j] == 2:
                    count += 1

        countlist.append(count)
        b = countlist.index(max(countlist))

    return valid[b]


def run_single_player():
    board = new_board()
    validp1 = valid_moves(board,1)
    validp2 = valid_moves(board,2)

    while len(validp1) > 0 and len(validp2) > 0:
        player = 1
        print_board(board)
        string = (input("\nYou are player 1. Where would you like to place your stone?"))

        if string == "q":
            quit()
        else:
            move = position(string)

        validp1 = valid_moves(board,1)
        validp2 = valid_moves(board,2)

        if player == 1:
            if move in validp1:
                next_state(board, player, move)
                player = 2
            elif move not in validp1:
                print("Invalid move")
                
        if player == 2:
            move = comp_best_move(board,2)
            next_state(board, player, move)

        if len(validp1) < 0 and len(validp2) < 0:
            (s1, s2) = score(board)
            if s1> s2:
                print("Congratuations, player 1, you have beaten player 2!")
                break
            elif s2 > s1:
                print("Congratulations, player 2, you have beaten player 1!")
                break
            




        


        



                     
        
