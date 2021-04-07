"""
Program for generating the list of edges of the database as a synthatically
correct text file
"""

# change this according to your machine
base = r"C:\Users\User\Desktop\Programming\Code Projects\Cadeira_Algoritmos\src\dijkstradutor"

in_file = open(base + r"\Database\unicodelang.txt")

out_file = open(base + r"\Create_graph\new_edgelist.py", 'w')
out_file.write("edge_list = [\n")

# convert txt to graph:
# ignore the first line
in_file.readline()
for line in in_file:
    country, lang, prob = line.split()
    out_file.write(f"\t({country}, {lang}, {prob}),\n")

out_file.write("]\n")

in_file.close()
out_file.close()

print('hi')
