#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 9 May 2019
#Assignment 2
#Task 2

expr = "(3.1 + 6*2^2) * (2 - 1)"


def tokenization(expr):
    
    numlist = ["1","2","3","4","5","6","7","8","9","0","."]
    whitesp = [" ",""]
    exprlist = list(expr)
    term = ""
    temp_list = []
    final_list = []

    for i in exprlist:
        if i in numlist:
            term += i
        else:
            temp_list.append(term)
            term = ""
            temp_list.append(i)
    temp_list.append(term)
            
    for i in temp_list:
        if i not in whitesp:
            final_list.append(i)
    
    for i in range(len(final_list)):
        if (final_list[i][0]).isdigit() == True: #[0] so that it works for float
            final_list[i] = float(final_list[i])
    
    return final_list

            
def has_precedence(op1, op2):
    
    operators = ["+", "-", "*", "/", "^"]
    rank = [1,1,2,2,3]
    id1 = 0
    id2 = 0

##    if op1 not in operators or op2 not in operators:
##        return False

    id1 = operators.index(op1)
    id2 = operators.index(op2)

    if rank[id1] == rank[id2]: # Returns True if operators are the same or + and - is used 
        return True

    return rank[id1] > rank[id2]


def simple_evaluation(tokens):

# Function to calculate each individual calculation in an equation
    def calculate(val1, op, val2):
        if op == "+":
            return val1+val2
        elif op == "-":
            return val1-val2
        elif op == "*":
            return val1*val2
        elif op == "/":
            return val1/val2
        elif op == "^":
            return val1**val2

    operators = ["+", "-", "*", "/", "^"]
    operatorlist = []
    idx = 0

    while (len(tokens) != 1):   # Repeats the operation until a single final value is returned
        for i in range(len(tokens)):    # Finds the index of the first operator of the equation and sets it as the highest precedence
            if tokens[i] in operators:
                precedence = tokens[i]
                idx = i
                break
            
        for i in range(len(tokens)):
            if tokens[i] in operators and has_precedence(precedence,tokens[i]) == False:    # Finds the operator that has the highest precedence in the equation by comparing each operator
                precedence = tokens[i]
                idx = i     # Finds the index of the operator with the highest precedence

                
        tokens[idx] = calculate(tokens[idx-1],tokens[idx],tokens[idx+1])
        tokens.pop(idx+1)
        tokens.pop(idx-1)
        
            
    return float(tokens[0])


def complex_evaluation(tokens):

    while "(" in tokens:
        bracket = []
        for i in range(len(tokens)):
            if tokens[i] == "(":
                start = i
            
        for i in range(len(tokens)):
            if tokens[i] == ")" and i>start:
                end = i
                break
            
            # Look for last open bracket, first close bracket, break when find first close bracket to prevent finding second close bracket
        for i in range(start+1,end):
            bracket.append(tokens[i])
            
        temp = simple_evaluation(bracket)
        tokens[start] = temp
        
        for i in range(end,start,-1):
            tokens.pop(i)
    else:
        final = simple_evaluation(tokens)
        
    return tokens[0]

def evaluation(string):

    tokens = tokenization(string)
    answer = complex_evaluation(tokens)

    return answer

