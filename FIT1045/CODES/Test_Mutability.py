#Mutability, Immutability, Identities of Object...

x = 2
y = 2
print("1-----------------")
print(x==y, id(x)==id(y))
print(x,y)

x = [1,2]
y = [1,2]
print("\n2-----------------")
print(x==y)
print(id(x)==id(y))
print(x,y)

x = [7,8,9]
y = x
z = y
print("\n3-----------------")
print(x==y and z==y, id(x)==id(y))
print(id(y)==id(z))
print(x,y,z)

x = [7,8,9]
y = x
z = y
y += x
print("\n4-----------------")
print(x==y and z==y)
print(id(x), id(y), id(z))
print(x,y,z)

x = [7,8,9]
y = x
z = y
y = x + [1]
print("\n5-----------------")
print(x==y and z==y)
print(id(x), id(y), id(z))
print(x,y,z)

x = [7,8,9]
y = x
z = y
y = x + y
print("\n6-----------------")
print(x==y and z==y)
print(id(x), id(y), id(z))
print(x,y,z)

from copy import copy
x = [1,2,3]
y = x[:]
z = copy(x)
print("\n7-----------------")
print(x==y and z==y)
print(id(x), id(y), id(z))
print(x,y,z)

y[0] = 5
z[0] = 100
print(x==y and z==y)
print(id(x))
print(id(y))
print(id(z))
print(x,y,z)

print("\n8-----------------")
from copy import copy
t1 = ['a','b']
t2 = t1[:]
t3 = copy(t1)
print("t1",t1,"t2",t2,"t3",t3)

t2[0] = 'A'
t3[0] = 'B'

print(t1[0])
print(t2[0])
print(t3[0])

print("\n9-----------------")
from copy import copy
t1 = [['a','b'],['c','d']]
     
t2 = t1[:]
t3 = copy(t1)
print("t1",t1,"t2",t2,"t3",t3)

t2[0][0] = 'A'
t3[0][0] = 'B'

print(t1[0][0])
print(t2[0][0])
print(t3[0][0])
