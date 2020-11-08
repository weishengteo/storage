#Name = Teo Wei Sheng
#Date = 8 March 2019
#Task 6: Strings

name = (input("Please input your name: "))
name = str.upper(name)
letters = len(name) - name.count(" ")
a = name.count("A")
e = name.count("E")
i = name.count("I")
o = name.count("O")
u = name.count("U")
print("Letters:" ,letters, " Number of A's: ",a, " Number of E's: ",e, " Number of I's: ",i," Number of O's: ",o," Number of U's: ",u)
