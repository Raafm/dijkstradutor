#olha as linhas na database
file = open(r'dijkstra_hiding_message\Database\unicodelang_country.txt','r')

#abre arquivo novo para por os nodes ao lado de seus nomes
new_file = open(r'dijkstra_hiding_message\Create graph\Nodes\Contries\countries.txt','w')


count = 1

for line in file:
    new_file.write('country node ' + str(count)+': ' + line + '\n')
    count+=1