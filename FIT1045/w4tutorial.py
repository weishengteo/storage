List = ("P","Y","T","H","O","N")

def min_index(List):
    index = 0
    for i in range(len(List)):
        if List[i] < List[index]:
            index = i
    return index

    
def selection_sort(List):
    for i in range(len(List)):
        index = min_index(List[i:])
        List[i], List[index+1] = List[index+1], List[i]
    return(List)

print(selection_sort(List))
            
        
