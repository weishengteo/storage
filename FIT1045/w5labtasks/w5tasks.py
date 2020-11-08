File = open("Tiny.txt","r")

final_list = []

def printList(list):
    for i in final_list:
        print(i[0], "kms, $",i[1])

def min_index(final_list):
    k = 0
    for i in range(1,len(final_list)):
        if final_list[i][0] < final_list[k][0]:
            k = i
    return k

def min_index2(final_list):
    k = 0
    for i in range(1,len(final_list)):
        if final_list[i][1] < final_list[k][1]:
            k = i
    return k

def selection_sort(final_list):
    for i in range(len(final_list)):
        j = min_index(final_list[i:]) + i
        final_list[i],final_list[j] = final_list[j],final_list[i]

def selection_sort2(final_list):
    for i in range(len(final_list)):
        j = min_index2(final_list[i:]) + i
        final_list[i],final_list[j] = final_list[j],final_list[i]

list = []
for line in File:
    list.append(line.strip().split(","))
for row in list:
    x = []
    for i in row:
        x.append(float(i))
    final_list.append(x)

selection = ""
while selection != "Quit":
    selection = input("Enter choice Print, Sort1(distance), Sort2 (price) or Quit: ")
    if selection == "Print":
        printList(list)
    elif selection == "Sort1":
        min_index(final_list)
        selection_sort(final_list)
    elif selection == "Sort2":
        min_index2(final_list)
        selection_sort2(final_list)
    elif selection == "Quit":
        quit()




