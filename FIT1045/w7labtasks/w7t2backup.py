#Name = Teo Wei Sheng
#Date = 19 April 2019
#Workshop 7
#Task 2

upper_bounds = [1,1,4]

def bounded_lists(upper_bounds):
    all = bitlists(upper_bounds)
    print(all)


def bitlists(n):
    first = (len(n))*[0]
    last = n
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1])]
    return res


def lex_suc(bitlst):
    res = bitlst[:]
    i = len(res) - 1
    while res[i] == 2:
        res[i] = 0
        i -= 1
    res[i] += 1
    return res
