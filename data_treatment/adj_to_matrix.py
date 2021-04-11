"""
Program for generating the adjacency matrix of the database from the created
adjacency list (adjacency.py). This is done for showing that popular graph
sites, such as, https://graphonline.ru/en/data_treatment_by_matrix , are not
capable of handling our input and solving the problem we solve.
"""

from pathlib import Path

# adj is the adjacency list of the graph that represents the database
# (the database can be found on dijkstradutor/Database)
from adjacency import adj

N = 868  # number of vertices. They are numbered 1 through N+1

# initializing the matrix with infinity values
matrix = [None]  # 1-indexed, not 0-indexed
for _ in range(N):
	# 1300 is the infinity value. Since there are 1255 edges in the database
	# and each has weight at most 1, 1300 can be safely taken as infinity.
	line = [1300]*(N+1)
	line[0] = None  # 1-indexed, not 0-indexed
	matrix.append(line)

# setting the weights of the entries of the matrix
for vertex in range(1, N+1):
	for neighbour, weight in adj[vertex]:
		matrix[vertex][neighbour] = weight

# base is the path to the dijkstradutor directory. This is necessary because
# the file needed (unicodelang_country.txt) is not in the current directory
# or in a subdirectory, so relative paths won't work.
base = str(Path().absolute().parent)
file = open(base+r"\data_treatment\matrix.txt", 'w')

for vertex in range(1, N+1):
	for neighbour in range(1, N+1):
		file.write(str(matrix[vertex][neighbour]) + ' ')
	file.write('\n')

file.close()
