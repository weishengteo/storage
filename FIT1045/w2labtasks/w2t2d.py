#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 2: Operations on sequences of integers
#Task2c

start = int(input("Where should I start?"))
stop = int(input("Where should I stop?"))
total = 0

for i in range(start,stop + 1):
    for j in range(1,i+1):
        value = (2*(int(i))**2) + (4*(int(j)))
        total = total + value

print("The result for the sum of the sums of 2i^2+4i from", start, "to", stop, "is: ", total)
