"""
Program for generating the adjacency matrix of the database from the created
adjacency matrix (adjacency.py). This is done for comparing the results given
by main.py with those given by https://graphonline.ru/en/create_graph_by_matrix ,
thus verifying the correctnes of the program.
"""

from adjacency import adj

N = 868  # number of vertices. They are numbere 1 through N+1

# initializing the matrix with infinity values
matrix = [None]  # 1-indexed, not 0-indexed
for _ in range(N):
	line = [1300]*(N+1)  # 1300 is the infinity value. See main.py for explanation
	line[0] = None  # 1-indexed, not 0-indexed
	matrix.append(line)

# setting the weights of the entries of the matrix
for vertex in range(1, N+1):
	for neighbour, weight in adj[vertex]:
		matrix[vertex][neighbour] = weight

# change this according to your machine
base = r"C:\Users\User\Desktop\Programming\Code Projects\Cadeira_Algoritmos\src\dijkstradutor"
file = open(base+r"\Create_graph\matrix.txt", 'w')

for vertex in range(1, N+1):
	for neighbour in range(1, N+1):
		file.write(str(matrix[vertex][neighbour]) + ' ')
	file.write('\n')

file.close()
