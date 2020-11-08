#Name = Teo Wei Sheng
#Student ID = 29800668
#Date = 31 May 2019
#Workshop 12
#Task 1

#write your code here

def is_clique(S, k, G):
    for i in S:
        for j in S:
            if G[i][j] == 0 and i != j:
                return False
    return True
    

def is_indset(S, k, G):
    for i in S:
        for j in S:
            if G[i][j] == 1 and i != j:
                return False
    return True
         
            

def complement(G):
    for i in range(len(G)):
        for j in range(len(G[0])):
            if i == j:
                continue
            elif G[i][j] == 0:
                G[i][j] = 1
            elif G[i][j] == 1:
                G[i][j] = 0
    
    return G


example_graph =\
               [[0, 1, 0, 0, 0, 0, 0],
		[1, 0, 1, 1, 0, 0, 0],
		[0, 1, 0, 1, 1, 1, 0],
		[0, 1, 1, 0, 1, 1, 0],
		[0, 0, 1, 1, 0, 1, 1],
		[0, 0, 1, 1, 1, 0, 1],
		[0, 0, 0, 0, 1, 1, 0]]

example_graph_complement =\
	       [[0, 0, 1, 1, 1, 1, 1],
		[0, 0, 0, 0, 1, 1, 1],
		[1, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0],
		[1, 1, 0, 0, 0, 0, 0],
		[1, 1, 1, 1, 0, 0, 0]]


if __name__ == "__main__":
	#if you have not yet implemented one of the functions, comment out those tests
	assert is_clique([2,3,4,5], 4, example_graph) == True
	assert is_clique([1,2,3], 2, example_graph) == True
	assert is_clique([1,2,3,6], 1, example_graph) == False
	assert is_clique([0,1,5,6], 5, example_graph) == False
	assert is_clique([1,2,3,4], 3, example_graph) == False

	assert is_indset([1,3,5], 2, example_graph) == False
	assert is_indset([1,2,6],2,  example_graph) == False
	assert is_indset([3,6], 2, example_graph) == True
	assert is_indset([1,2,3,6], 1, example_graph) == False
	assert is_indset([0,2,6], 2, example_graph) == True

	assert complement(example_graph) == example_graph_complement

	print("All tests passed!")
