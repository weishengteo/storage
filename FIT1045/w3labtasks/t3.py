#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 3: Assignment and indexing
#Task3

a_list = []

count  = 0
while count < 5:
    a_list.append(count)
    a_list[count] = count
    count = count + 1

print(a_list)



