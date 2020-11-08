def knapsack(capacity,values,w):
    final = []
    for i in range(len(values)-1,-1,-1):
        if capacity - w>= 0:
            final.append(values[i])
            capacity -= w
        else:
            break
    return(sum(final))

print(knapsack(12,[1,6,9,34,67,77],5))
