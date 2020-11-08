#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 3 May 2019
#Workshop 8
#Task 1

a_list = [1,2,3,4,5,6,7]

def recursive_reserve(a_list):
    n = len(a_list)
    if n == 0:
        return []
    else:
        return [a_list[-1]] + recursive_reserve(a_list[:n-1])
        
