#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 9 May 2019
#Workshop 8
#Task 3

a_list = [1,2,5,7,9,11,13,17,54,79,101]
target = 54

def simple_recursive_binary_search(a_list, target):

    hi = len(a_list)-1
    lo = 0
    
    if hi - lo < 2:
        if a_list[hi] == target:
            return True
        elif a_list[lo] == target:
            return True
        else:
            return False
        
    mid = int((hi - lo)/2)

    if a_list[mid] == target:
        return True
    elif a_list[mid] < target:
        return simple_recursive_binary_search(a_list[mid:], target)
    else:
        return simple_recursive_binary_search(a_list[:mid+1], target)


def advanced_recursive_binary_search(a_list, target, lo, hi):

    if hi - lo < 2:
        if a_list[hi] == target:
            return hi
        elif a_list[lo] == target:
            return lo
        else:
            return None
        
    mid = int(lo + ((hi - lo)/2))

    if a_list[mid] == target:
        return mid
    elif a_list[mid] < target:
        return advanced_recursive_binary_search(a_list, target, mid+1, hi)
    else:
        return advanced_recursive_binary_search(a_list, target, lo, mid-1)


