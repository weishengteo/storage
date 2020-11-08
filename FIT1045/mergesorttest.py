lst = [2,33,8,9]
def merge_sort(lst):
    k,n = 1,len(lst)
    while k<n:
        nxt = []
        for a in range(0,n,2*k):
            b,c = a+k, a+2*k
            nxt += merge(lst[a:b],lst[b:c])
        lst = nxt
        k = 2 * k
    return lst
    
def merge(l,r):
    res = []
    n1,n2 = len(l), len(r)
    i,j = 0,0
    while i<n1 and j<n2:
        if l[i] <= r[j]:
            res += [l[i]]
            i+=1
        else:
            res += [r[j]]
            j+=1
    return res + l[i:] + r[j:]

print(merge_sort(lst))
