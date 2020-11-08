#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 14 May 2019
#Workshop 9
#Task 1


def basic_matching(str):
    strlist = list(str)
    a = strlist.pop()
    if a == ")" and strlist[0] == "(":
        return True
    return False

def matching(str):
    opening = "[{("
    closing = "]})"
    stack = []
    obrac = ""
    cbrac = ""
    strlist = list(str)

    if len(strlist) == 0:
        return False
    
    for i in range(len(strlist)):
        
        if strlist[i] in opening:
            stack.append(strlist[i])
            
        elif strlist[i] in closing:
            obrac = stack.pop()
            cbrac = opening[closing.index(strlist[i])]
            if obrac != cbrac:
                return False
    return True

print(basic_matching("()"))                           
print(matching("[(({}))]()"))
