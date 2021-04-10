"""
Program for generating the adjacency list of the database as a synthatically
correct text file. Do not run it more than once.
"""

from pathlib import Path

# base is the path to the dijkstradutor directory. This is necessary because
# the file needed (unicodelang.txt) is not in the current directory
# or in a subdirectory, so relative paths won't work.
base = str(Path().absolute().parent)

in_file = open(base+r"\Database\unicodelang.txt", 'r')

# there are 868 nodes, numbered from 1 to 868
adj = []
for _ in range(869):
	adj.append([])

# ignoring the first line
in_file.readline()
for line in in_file:
	line = line.split()
	country = int(line[0]) + 614
	lang = int(line[1])
	prob = float(line[2])
	# edges with no database-weight are ignored (they simply mean that country
	# doesn't speak lang)
	if prob > 0:
		# an edge with database-weight greater than 0 from a country to a lang
		# costs nothing from the point of view of the problem this program 
		# intends to solve, so they are assigned weight 0
		adj[country].append((lang, 0))
		adj[lang].append((country, prob))

in_file.close()

out_file = open("adjacency.py", 'w')
out_file.write("adj = [\n")
for tup in adj:
	out_file.write(str(tup) + ",\n")
out_file.write("]\n")

out_file.close()
