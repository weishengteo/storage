#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 17 May 2019
#Workshop 10
#Task 1

a_list = [1,0,6,3,-1,7]

def quicksort(a_list):

    low = []
    high = []
    
    if len(a_list) <= 1:
        return a_list

    pivot = a_list[0]

    for i in range(len(a_list)):
        if a_list[i] < pivot:
            low.append(a_list[i])
        elif a_list[i] > pivot:
            high.append(a_list[i])

    return quicksort(low) + [pivot] + quicksort(high)

print(quicksort(a_list))
