"""
Program for generating the list of edges of the database as a synthatically
correct text file
"""

from pathlib import Path

# base is the path to the dijkstradutor directory. This is necessary because
# the file needed (unicodelang.txt) is not in the current directory
# or in a subdirectory, so relative paths won't work.
base = str(Path().absolute().parent)

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
