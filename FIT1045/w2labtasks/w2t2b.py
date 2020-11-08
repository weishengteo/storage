#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 2: Operations on sequences of integers
#Task2b

start = int(input("Where should I start?"))
stop = int(input("Where should I stop?"))
total = 0

for index in range(start , stop + 1):
    value = 3*(int(index))
    total = total + value

print("The result for sum of 3i from", start, "to", stop, "is: ", total)
