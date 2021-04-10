"""
Program for generating the correspences between integers and languages.
"""
from pathlib import Path

# base is the path to the dijkstradutor directory. This is necessary because
# the file needed (unicodelang.language.txt) is not in the current directory
# or in a subdirectory, so relative paths won't work.
base = str(Path().absolute().parent.parent.parent)

# olha as linhas na database
file = open(base + r"\Database\unicodelang.language.txt",'r')

# abre arquivo novo para por os nodes ao lado de seus nomes
new_file = open(base + r"\Create_graph\Nodes\Languages\languages.txt",'w')

count = 1

for line in file:
    new_file.write(str(count) + ' ' + line)
    count+=1

file.close()
new_file.close()
