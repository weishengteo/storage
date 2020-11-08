#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 2: Operations on sequences of integers
#Task2c

start = int(input("Where should I start?"))
stop = int(input("Where should I stop?"))
ivalue = int(input("Valid i values are those divisible by..."))
total = 0

for index in range(start , stop + 1):
    if index % ivalue == 0:
        value = (2*(int(index))**2) + (4*(int(index)))
        total = total + value

print("The result for sum of 2i^2+4i from", start, "to", stop, "(with i values divisible by" , ivalue, ") is: ", total)
