#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 5: Using Lists
#Task5

import random

my_list = []

for i in range(1,1001):
    x = random.randint(1,6)
    my_list.append(x)
    
mean = (sum(my_list))/(len(my_list))

print(my_list,mean)
