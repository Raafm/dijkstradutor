"""
Program for generating the correspences between integers and languages.
"""

# change this according to your machine
base = r"C:\Users\User\Desktop\Programming\Code Projects\Cadeira_Algoritmos\src\dijkstradutor"

# olha as linhas na database
file = open(base + r'\Database\unicodelang.language.txt','r')

# abre arquivo novo para por os nodes ao lado de seus nomes
new_file = open(base + r'\Create_graph\Nodes\Languages\languages.txt','w')

count = 1

for line in file:
    new_file.write(str(count) + ' ' + line)
    count+=1

file.close()
new_file.close()
