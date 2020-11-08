#Min_index of Selection Sort

def min_index(List):
    for j in range(1,len(List)):
        if List[j-1]>List[j]:
            index = j
    return index

print(min_index([2,4,1,3]))
