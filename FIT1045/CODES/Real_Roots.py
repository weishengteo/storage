from math import sqrt

def real_roots(a,b,c):
    d = b*b-4*a*c
    if d < 0:
        return 0,[None]
    elif d == 0:
        return 1,[-b/2*a]
    else:
        return 2,[(-b+sqrt(d))/(2*a),(-b-sqrt(d))/(2*a)]

no,val=real_roots(1,1,-4)
print("There are {} real roots: {}".format(no,val))
