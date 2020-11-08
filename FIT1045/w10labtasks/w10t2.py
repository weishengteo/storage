#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 23 May 2019
#Workshop 10
#Task 2

t = [ ( 2 , 1 ) , ( 3 , None ) , ( 5 , 4 ) , ( None , None ) , ( None , None ) , ( None , None ) ]

def count(t,v):
    mycount = 1
    if v is None:
        return 0
    else:
        left, right = t[v]
        mycount += count(t,left)
        mycount += count(t,right)
    return mycount

print(count(t,0))

##def count(t,v):
##    mycount = 1
##    if v is None:
##        return 0
##    else:
##        left, right = t[v]
##        print(left)
##        leftindex = t.index(left)
##        rightindex = t.index(right)
##        mycount += count(t,leftindex)
##        mycount += count(t,rightindex)
##
##    return mycount

def balance(t,v):
    left, right = t[v]
    return count(t,left) - count(t,right)

##def count(t,v):
##    if v is None:
##        return 0
##    if v < len(t):
##        left, right = t[v]
##    else:
##        return 0
##    if v is not None:
##        mycount = 1
##        if left is not None:
##            leftindex = 2*v + 1
##            mycount += count(t,leftindex)
##        if right is not None:
##            rightindex = 2*v + 2
##            mycount += count(t,rightindex)
##    return mycount
##    
##print(count(t,0))

##def count(t,v):
##    if v is None:
##        return 0
##    if v < len(t):
##        left, right = t[v]
##        print(left)
##    else:
##        return 0
##    if v is not None:
##        mycount = 1
##        leftindex = 2*v + 1
##        rightindex = 2*v + 2
##        mycount = 1 + count(t,leftindex)
##        mycount = 1 + count(t,rightindex)
##    return mycount

##def count(t,v):
##    mycount = 1
##    if v is None:
##        return 0
##    else:
##        for i in range(len(t[v])):
##            print(t[v])
##            mycount += count(t,t[v][i])
##        return mycount
