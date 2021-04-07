from edgelist import edge_list

N = 868                     #tem 868 nodes, mas o node 0 na verdade == 1, entao CUIDADO COM OVERFLOW

Graph = list()
n = N+1
for i in range(n):
    Graph.append([])

for edge in edge_list:
    Graph[edge[0]].append( [edge[1], edge[2]] )               #parece que temos alguns nodes nao usados, se possivel olhar eles depois
    Graph[edge[1]].append( [edge[0], edge[2]] )               

print("inicio: ")

Graph_file = open(r'dijkstra_hiding_message\Create_graph\Graph.txt','w')

count = 0
for node in Graph:
    Graph_file.write(str(count) + ":   [\n")
    count += 1
    for vizinho in node:
        Graph_file.write('node: ')
        Graph_file.write(str(vizinho[0]))
        formating = ", proportion = "
        Graph_file.write(formating.center(20,' '))
        Graph_file.write(str(vizinho[1]))
        Graph_file.write("\n")
    Graph_file.write("]\n\n")

