def race(precision, algorithms):
    race_list = []
    count = 0
    for algo in range(len(algorithms)):
        if algorithms[algo] == taylor:
            race_list.append(taylor(precision))
        elif algorithms[algo] == wallis:
            race_list.append(wallis(precision))
        elif algorithms[algo] == basel:
            race_list.append(basel(precision))
        elif algorithms[algo] == spigot:
            race_list.append(spigot(precision))

            return race_list


        def race(precision, algorithms):
    race_list = []
    final_list = []
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

        for term in race_list.sort():
            final_list.append(tuple([

        
player = 0
def player():
    choice = print("Do you want to play as Player 1 or Player 2?")
    if choice == "Player 1":
        player = 1
    elif choice == "Player 2":
        player = 2
    return player


        
