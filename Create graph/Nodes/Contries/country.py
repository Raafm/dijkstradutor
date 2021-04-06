#olha as linhas na database
file = open(r'dijkstra_hiding_message\Database\unicodelang_country.txt','r')

#abre arquivo novo para por os nodes ao lado de seus nomes
new_file = open(r'dijkstra_hiding_message\Create graph\Nodes\Contries\countries.txt','w')

#os paises comecam no node 615, pois o ultimo idioma  == node 614
count = 615 

for line in file:
    new_file.write('node ' + str(count)+': ' + line + '\n')
    count+=1