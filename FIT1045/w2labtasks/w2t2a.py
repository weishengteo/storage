#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 2: Operations on sequences of integers
#Task2a

start = 1
end = 10
total = 0

for index in range(start,end+1):
    value = 3*(int(index))
    total += value

print(total)
