"""
Program for generating the correspences between integers and countries.
"""

# change this according to your machine
base = r"C:\Users\User\Desktop\Programming\Code Projects\Cadeira_Algoritmos\src\dijkstradutor"

# olha as linhas na database
file = open(base + r'\Database\unicodelang_country.txt','r')

# abre arquivo novo para por os nodes ao lado de seus nomes
new_file = open(base + r'\Create_graph\Nodes\Contries\countries.txt','w')

# os paises comecam no node 615, pois o ultimo idioma  == node 614
count = 615 

for line in file:
    new_file.write(str(count) + ' ' + line)
    count+=1

file.close()
new_file.close()
