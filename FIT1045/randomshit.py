board = new_board()
board[5][2] = "2"
enclosing(new_board(),2,(2,5),(1,-1))
print_board(board)

;
def next_state(board,player,pos):
    direction_list =[[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    direction_used = []
    if player == 1:
        enemy = 2
    else:
        enemy = 1
     
    for z in range(8):
        direction = direction_list[z]
        if enclosing(board,player,pos,direction) == True:
            direction_used.append(direction)
            x = direction
            direction_used.append(x)
        else:
            continue
        
    next_board = board
    x_val = pos[0]
    y_val = pos[1]
    for i in range (len(direction_used)):
        current_direction = direction_used[i]
    
        while board[x_val][y_val] != player:
            board[x_val][y_val] = player
            x_val = x_val + current_direction[0]
            y_val = y_val + current_direction[1]
            
            
    if player == 2:
        if valid_moves(next_board,1) != []:
            next_player = 1
    elif player == 1:
        if len(valid_moves(next_board,2)) > 0:
            next_player = 2
    elif len(valid_moves(next_board,1)) == 0 and len(valid_moves(next_board,2)) == 0:
        next_player = 0
        
                                             
    return next_board, next_player
            
    

def position(string):
    string = str(string)
    list_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    list_numbers = ["1","2","3","4","5","6","7","8"]
    number1 = None
    number2 = None
    if len(string) > 2 or len(string) <= 1:
        return None
    for i in range(8):
        if string[0] == list_letters[i]:
            number1 = list_letters.index(string[0])
        else:
            continue
    
    for j in range(8):
        if string[1] == str(list_numbers[j]):
            number2 = list_numbers.index(string[1])
        else:
            continue
        
    pos = number2, number1
    if None in pos:
        return None
    else:
        return pos
    
            

    

def run_two_player():
    player = int(input("Who starts first, player 1(b) or 2(w)? " ))
    if player == 2:
        player = 1

    print("Its player 1's turn")
    print_board(new_board())
    next_board = new_board()
    while True:
            
        string = input("Please input position ")
        pos = position(string)
       

        if string == "q" or valid_moves(next_board,player) == []:
            scr = score(next_board)
            print("White scored ", scr[1], " points")
            print("Black scored ", scr[0], " points")
            if scr[1] > scr[0]:
                print("White wins! Better luck next time!")
            elif scr[0] > scr[1]:
                print("Black wins! ")
            else:
                print("Draw!")
            
            quit
            break
        

        if pos not in valid_moves(next_board,player):
            while pos not in valid_moves(next_board,player):
                print("Invalid move")
                string = input("Please input a position ")
                if string == "q":
                    scr = score(next_board)
                    print("White scored ", scr[1], " points")
                    print("Black scored ", scr[0], " points")
                    if scr[1] > scr[0]:
                        print("White wins! Better luck next time!")
                    elif scr[0] > scr[1]:
                        print("Black wins! ")
                    else:
                        print("Draw!")

                    input("Press to exit")
                    quit
                    break
                    
                else:
                    pos = position(string)
                
        next_board = next_state(next_board,player,pos)[0]
        board = next_board
        player = next_state(next_board,player,pos)[1]
        print_board(next_board)
        
        for i in range(0,8):
            for j in range(0,8):
                if board[i][j] == "w":
                    board[i][j] = 2
                elif board[i][j] ==  "b":
                    board[i][j] = 1
                else:
                    board[i][j] = 0
    

            
        print("The next player is player", player)
        
    


run_two_player()
input("Press enter to exit")
