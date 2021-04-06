
file = open(r'Database\unicodelang.txt','r')

#1255

edge_list = list()
country = ''
language = ''

#convert txt to graph:
count=0
probability = ''
for line in file:
    if "%" in line: continue
    else: 
        line = line.split('\t')
        country = int(line[0])
        language = int(line[1])
        probability = float(line[2][:len(line[2]) - 1])

    edge_list.append([country,language,probability])
         

print(edge_list)
print( "fim: ")
print(edge_list[len(edge_list)-1])
