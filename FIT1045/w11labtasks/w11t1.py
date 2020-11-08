#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 28 May 2019
#Workshop 11
#Task 1

heap = [1,3,2,7,4,8]

def min_child(v, heap):
    left = 2*v + 1
    right = 2*v + 2
    if right>len(heap)-1 and left<=len(heap)-1:
        return left
    elif heap[right]> heap[left]:
        return left
    elif heap[left]> heap[right]:
        return right
    
def insert(heap, item):
    heap.append(item)
    currenti = len(heap) - 1
    parent = (currenti-1)//2
    while currenti > 0 and heap[parent] > heap[currenti]:
        heap[parent] , heap[currenti] = heap[currenti], heap[parent]
        currenti = parent
        parent = (currenti-1)//2
    return heap
        
def extract_min(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    extracted = heap.pop()
    v = 0
    left = (2*v)+1
    right = (2*v)+2
##    while heap[v] > heap[left] or heap[v] > heap[right]:
    while left <= len(heap)-1 or right < len(heap)-1:
        
        if heap[v] > heap[left] and right > len(heap)-1:
            heap[v], heap[left] = heap[left], heap[v]
            v = left
            left = (2*v)+1
            right = (2*v)+2
            
        elif right <= (len(heap))-1:
            if heap[v] > heap[left] and heap[v] > heap[right]:
                if heap[left] > heap[right]:
                    heap[v], heap[right] = heap[right], heap[v]
                    v = right
                    left = (2*v)+1
                    right = (2*v)+2
                else:
                    heap[v], heap[left] = heap[left], heap[v]
                    v = left
                    left = (2*v)+1
                    right = (2*v)+2
                    
            elif heap[v] > heap[left] and heap[v] < heap[right]:
                heap[v], heap[left] = heap[left], heap[v]
                v = left
                left = (2*v)+1
                right = (2*v)+2
                
            elif heap[v] < heap[left] and heap[v] > heap[right]:
                heap[v], heap[right] = heap[right], heap[v]
                v = right
                left = (2*v)+1
                right = (2*v)+2
        else:
            break
            
    return extracted, heap

def heapsort(items):
    newitems = []
    for i in range(len(items)):
        a = items.pop()
        insert(newitems,a)
    
    sortedlist = []
    while len(newitems) != 0:
        res = extract_min(newitems)
        sortedlist.append(res[0])
        newitems = res[1]
    return sortedlist
