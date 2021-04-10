"""
Program for generating the correspences between integers and countries.
"""

from pathlib import Path

# base is the path to the dijkstradutor directory. This is necessary because
# the file needed (unicodelang_country.txt) is not in the current directory
# or in a subdirectory, so relative paths won't work.
base = str(Path().absolute().parent.parent.parent)

# olha as linhas na database
file = open(base + r'\Database\unicodelang_country.txt','r')

# abre arquivo novo para por os nodes ao lado de seus nomes
new_file = open(base + r'\Create_graph\Nodes\Countries\countries.txt','w')

# os paises comecam no node 615, pois o ultimo idioma  == node 614
count = 615 

for line in file:
    new_file.write(str(count) + ' ' + line)
    count+=1

file.close()
new_file.close()
