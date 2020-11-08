#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 1: Flipping coins
#Task1a

import random
n = int(input("How many times would you like to flip the coin?"))
heads = 0
tails = 0
        
for index in range(n):
    num = (random.random())
    if num < 0.5:
        heads = heads + 1
    else:
        tails = tails + 1

ratio = (heads/n)

print("Number of heads: ", heads, "Number of tails: ", tails)
print("Ratio: ", ratio)


