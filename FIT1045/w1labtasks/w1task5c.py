#Name = Teo Wei Sheng
#Date = 8 March 2019
#Task 5: Flipping coins
#Task5c

import random

count = 0

p = float(input("What kind of bias do your coins have?"))

while count < 3:
    num = (random.random())
    if num < p:
        heads = ("True")
    else:
        heads = ("False")
    
    count = count+1
      
    print ("Count flip ",count, " has a value of heads:", heads)
