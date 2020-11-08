#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 19 April 2019
#Workshop 7
#Task 2
#Question 1

upper_bounds = [1,7,5]

def bounded_lists(upper_bounds):
    all = bitlists(upper_bounds)
    print(all)

def bitlists(n):
    first = (len(n))*[0]
    last = n
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1],n)]
    return res


def lex_suc(bitlst,n):
    res = bitlst[:]
    i = len(res) - 1
    while res[i] == n[i]:
        res[i] = 0
        i -= 1
    res[i] += 1
    return res

