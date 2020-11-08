#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 19 April 2019
#Workshop 7
#Task 2
#Question 2

def brute_force_coin_exchange(amount, denominations):
    num = []
    mycount = []
    feasible = []
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

    for i in range(len(denominations)):
        num.append(amount//denominations[i])
    all = bitlists(num[::-1])

    def feasiblility(all,denominations):
        for i in range(len(all)):
            mysum = 0
            for j in range(len(all[0])):
                mysum += all[i][j]*denominations[j]
            if mysum == amount:
                feasible.append(all[i])
            else:
                continue
        return feasible

    feasible = feasiblility(all,denominations)
    for i in range(len(feasible)):
        mycount.append(sum(feasible[i]))

    minindex = mycount.index(min(mycount))
    print(feasible[minindex])

            
