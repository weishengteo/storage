#Name = Teo Wei Sheng
#Date = 15 March 2019
#Assignment 1
#Task 1: Race to pi

import math

#Basel problem
def basel(precision):
    basel_n = 0
    basel_addition = 0
    basel_result = 0
    
    while abs(math.pi - basel_result) >= precision:
        basel_n = basel_n + 1
        basel_addition = basel_addition + ((6*(1/((basel_n)**2))))
        basel_result = math.sqrt(basel_addition)
        
    return (basel_result, basel_n)

#Taylor expansion
def taylor(precision):
    taylor_n = 0
    taylor_nume = 0
    taylor_denom = 1
    taylor_result = 0

    while abs(math.pi - taylor_result) >= precision:
        taylor_n = taylor_n + 1
        
        if (taylor_n) % 2 == 0:
            taylor_nume = -1
        else:
            taylor_nume = 1
            
        taylor_result = taylor_result + (4*(taylor_nume / taylor_denom))
        taylor_denom = taylor_denom + 2

    return(taylor_result, taylor_n)

#Wallis algorithm
def wallis(precision):
    wallis_n = 0
    wallis_count = 2
    wallis_result = 1
    
    while abs(math.pi - wallis_result) >= precision:
        wallis_n = wallis_n + 1
        wallis_result *= (wallis_count*wallis_count)/((wallis_count - 1)*(wallis_count + 1))
        wallis_result *= 2
        wallis_count += 2
        
        if (math.pi - wallis_result) < precision:
            wallis_result /= 2
        else:
            continue

    return(wallis_result, wallis_n)

#Spigot algorithm
def spigot(precision):
    spigot_list = []
    spigot_n = 0
    spigot_result = 0
    spigot_denom = 1
    spigot_nume = 1
    spigot_terms = 1
    spigot_final = 0

    while abs(math.pi - (spigot_final)*2) >= precision:

        spigot_n += 1
        spigot_result = ((spigot_nume)/(spigot_denom))
        spigot_terms *= spigot_result
        spigot_list.append(spigot_terms)

        if spigot_n > 1:
            spigot_nume += 1
            
        spigot_denom += 2
        spigot_final = sum(spigot_list)

    return ((spigot_final)*2, spigot_n)
    
#Race algorithm
def race(precision, algorithms):
    race_list = []
    count = 0

    for algo in range(len(algorithms)):
        if algorithms[algo] == taylor:
            race_list.append(taylor(precision)[1])
        if algorithms[algo] == wallis:
            race_list.append(wallis(precision)[1])
        if algorithms[algo] == basel:
            race_list.append(basel(precision)[1])
        if algorithms[algo] == spigot:
            race_list.append(spigot(precision)[1])

    final_list = list(enumerate(race_list,1))
    final_list.sort(key=lambda tup: tup[1])
    
    return final_list

#Print results algorithm
def print_results(final_list):
    for result in range(len(final_list)):
        print("Algorithm", (final_list[result])[0], "finished in", (final_list[result])[1], "steps")

    
