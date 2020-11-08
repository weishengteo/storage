#Name = Teo Wei Sheng
#Date = 15 March 2019
#Task 4: Lists of Lists, Tables and References
#Task4

final_list = []

for i in range(1,6):
    user_input = str(input("Enter some numbers:"))
    user_split = list(user_input.split())
    my_list = [int(i) for i in user_split]
    final_list.append(my_list)
    
print(final_list)
