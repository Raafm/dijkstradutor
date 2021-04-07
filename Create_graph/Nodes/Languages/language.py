file = open(r'dijkstra_hiding_message\Database\unicodelang.language.txt','r')

new_file = open(r'dijkstra_hiding_message\Create graph\Nodes\Languages\languages.txt','w')

count = 1

for line in file:
    new_file.write('node ' + str(count)+': ' + line + '\n')
    count+=1