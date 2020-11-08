#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 3 May 2019
#Workshop 8
#Task 2

def simple_recursive_power(x,n):
    if n == 0:
        return 1
    else:
        return x * simple_recursive_power(x,(n-1))

def advanced_recursive_power(x,n):
    if n == 0:
        return 1
    else:
        if (n % 2 == 0):
            return advanced_recursive_power(x,(n/2)) * advanced_recursive_power(x,(n/2))
        else:
            return x * advanced_recursive_power(x,(n-1))
            
