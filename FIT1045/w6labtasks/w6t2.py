#Name = Teo Wei Sheng
#Date = 17 April 2019
#Task 2

def greedy_coin_change(amount, denoms):
    n = len(denoms)

    coins = sorted(denoms, reverse=True)

    denom = [0]*n
    total = 0
    for i in range(len(coins)):
        while total + coins[i] <= amount:
            total += coins[i]
            denom[i] += 1
        else:
            continue
    return denom[::-1]
