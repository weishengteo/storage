def f(x):
    return x*x-5

def iter_bisec(a,b,e):
    m = (a+b)/2
    while abs(f(m)) > e:
        if f(m)*f(b) < 0:
            a = m
        else:
            b = m
        m = (a+b)/2
    return m

a = 1
b = 3
e = 0.01
print(iter_bisec(a,b,e))



def recur_bisect(a,b,e):
    m = (a+b)/2

    if abs(f(m)) < e:
        return m

    else:
        if f(m)*f(b) < 0:
            a = m
            return recur_bisect(a,b,e)
        else:
            b = m
            return recur_bisect(a,b,e)

print(recur_bisect(a,b,e))
    
