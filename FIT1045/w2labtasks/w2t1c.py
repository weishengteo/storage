#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 1: Flipping coins
#Task1c

import random
n = int(input("How many times would you like to flip the coin?"))
heads = 0
tails = 0
others = 0
        
for index in range(n):
    num = (random.randrange(0,3))
    if num == 0:
        heads = heads + 1
    elif num == 1:
        tails = tails + 1
    else:
        others = others + 1

print("Number of heads: ", heads, "Number of tails: ", tails, "Number of others: ", others)
