def changeslowHelper(coinList, value):
    
    def changeslow(coins, change):

        minCoins = [0 for c in coins]
        minCoins[0] = change
        # now we recursively step through the algorithm at every level
        # and find the minimum amount for that level
        for coin in [c for c in coins if c <= change]:
            temp = (changeslow(coins, change - coin))
            temp[coins.index(coin)] += 1
            if sum(minCoins) > sum(temp):
                minCoins = temp
                bestSum = temp
        return (minCoins)
    
        
    finalCoins = changeslow(coinList, value)
    
    coinSum = sum(finalCoins)
    
    return (finalCoins, coinSum)


    




coins =[1,2,5]

print (changeslowHelper(coins, 15))
