#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 3: Rock, Paper, Scissors
#Task3

import random
def beats(choice1,choice2):
    if choice1 == "ROCK" and choice2 == "SCISSORS":
        result = "You win!"
    elif choice1 == "PAPER" and choice2 == "ROCK":
        result = "You win!"
    elif choice1 == "SCISSORS" and choice2 == "PAPER":
        result = "You win!"
    elif choice1 == choice2:
        result = "You draw!"
    elif choice1 == "ROCK" and choice2 == "PAPER":
        result = "You lose!"
    elif choice1 == "PAPER" and choice2 == "SCISSORS":
        result = "You lose!"
    elif choice1 == "SCISSORS" and choice2 == "ROCK":
        result = "You lose!"
    else:
        result = "Invalid input"
    return result

choice1 = 0

while choice1 != "QUIT":
    choice1 = str(input("What do you choose?"))
    choice1 = choice1.upper()
    num = (random.randrange(0,3))
    if num == 0:
        choice2 = "ROCK"
    elif num == 1:
        choice2 = "PAPER"
    else:
        choice2 = "SCISSORS"    
    if choice1 != "QUIT":
        print("Your opponent chose", choice2, "... ", beats(choice1,choice2))
        continue
    else:
        quit()
        
        


    
