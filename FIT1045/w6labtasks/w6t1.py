#Name = Teo Wei Sheng
#Date = 17 April 2019
#Task 1


def greedy_items(values, weights, capacity, pref):
    n = len(values)

    if pref == 1:
        def l_weight(i): return values[i]
        items = sorted(range(n), key=l_weight, reverse=False)
            
        sel, value, weight = [], 0, 0
        for i in items:
            if weight + weights[i] <= capacity:
                sel += [i]
                weight += weights[i]
                value += values[i]
        return sel, value, weight

    elif pref == 2:
        def score(i): return values[i]
        items = sorted(range(n), key=score, reverse=True)

        sel, value, weight = [], 0, 0
        for i in items:
            if weight + weights[i] <= capacity:
                sel += [i]
                weight += weights[i]
                value += values[i]
        return sel, value, weight

    elif pref == 3:
        def inv_weight(i): return 1/weights[i]
        items = sorted(range(n), key=inv_weight, reverse=True)

        sel, value, weight = [], 0, 0
        for i in items:
            if weight + weights[i] <= capacity:
                sel += [i]
                weight += weights[i]
                value += values[i]
        return sel, value, weight

    elif pref == 4:
        def val_per_kg(i): return values[i]/weights[i]
        items = sorted(range(n), key=val_per_kg, reverse=True)

        sel, value, weight = [], 0, 0
        for i in items:
            if weight + weights[i] <= capacity:
                sel += [i]
                weight += weights[i]
                value += values[i]
        return sel, value, weight



def process_file(filename):
    list = []
    final_list = []
    weights = []
    values = []
    File = open(filename,"r")

    for line in File:
        line = line.replace("kg","").replace("$","")
        list.append(line.strip().split(" "))
        
    for row in list:
        x = []
        for i in row:
            x.append(int(i))
        final_list.append(x)

    for j in range(len(final_list)):
        weights.append(final_list[j][0])
        values.append(final_list[j][1])

    return (weights, values)

filename = input("Please enter file name with item details: ")
capacity = int(input("Please enter the capacity of the knapsack: "))
pref = int(input("Please enter your preferred approach: least weights = 1, most value = 2, inverse weight = 3, most value/weight = 4 : "))
(weights, values) = process_file(filename)
(sel, value, weight) = greedy_items(values, weights, capacity, pref)
list.sort(sel)

if len(sel) == 1:
    print("Optimal answer: item", sel[0]+1, ", value =" ,value, "$")
elif len(sel) == 2:
    print("Optimal answer: item", sel[0]+1, "and item", sel[1]+1, ", value =" ,value, "$")
elif len(sel) == 3:
    print("Optimal answer: item", sel[0]+1, ",item", sel[1]+1, "and item", sel[2]+1 ,", value =" ,value, "$")
elif len(sel) == 4:
    print("Optimal answer: item", sel[0]+1, ",item", sel[1]+1, ",item", sel[2]+1, "and item", sel[3]+1, ", value =" ,value, "$")

        
