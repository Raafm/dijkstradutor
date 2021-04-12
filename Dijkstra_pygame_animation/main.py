# built-in
import time

# third-party
import pygame

# local (from this project)
from groundwork.graph_countries_data import mini_graph as graph, nodes, edge_list, num_sigla, edge_dict
from groundwork.draw_graph import display_graph
# from groundwork.graph import test_graph as graph
# from groundwork.graph import nodes, edge_dict
from groundwork.heap import Heap
from groundwork.colors import *
# fiz um arquivo com as cores em rgb, 
# podemos pegar de la as cores que formos usar.
# Mesmo se vc achar que nao vai usar, nao apague as outras cores,
# pois talvez vc mude de ideia sobre as melhores cores para o node.
# As cores atualmente em uso aqui são as importadas acima

color_unvisited = White         # se modificar esse tme que modificar no arquivo graph tambem, ou fazer funcao para  modificar aqui
color_current_node = Gray
color_visited   = Black	    
color_current_edge = Cyan
node_number_color = Red
number_size = 15

INFINITY = 1000000
time_delay = 1               # tempo referencia para o codigo parar apos atualizar a tela

source = int(input("Source: "))                                #    TRATAR ERROS DE INPUT
destination = int(input("Destination: "))

pygame.init()

screen = pygame.display.set_mode((900,700))

nodes[source][0] = Blue  # initial color of source

display_graph(screen,graph,nodes,edge_dict, num_sigla)                    # display inicial da tela

time.sleep(time_delay)

# running dijkstra
cost = [INFINITY]*(len(nodes)+1)
cost[source] = 0

# the parent of a node in the shortest path to it from source
parent = [None]*(len(nodes)+1)

# this defines a min priority queue (pq) of pairs for use in the Dijkstra.
# The pairs used will be of the form (distance_from_source, vertex).
pq = Heap(comp=lambda tuple1, tuple2: tuple1[0] > tuple2[0])
pq.insert( (0, source) )

# this is the dijkstra loop as well as the animation loop
while not pq.empty():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                exit()

    curr_node_cost, curr_node = pq.pop()           # "curr" stands for "current"
    if curr_node_cost > cost[curr_node]:
        print("hi")
        continue

    nodes[curr_node][2] += 10                      # aumenta tamanho do node

    if curr_node != source:
        nodes[curr_node][0] = color_current_node   # indica a visita ao node

    display_graph(screen,graph,nodes,edge_dict,num_sigla)             # atualiza a tela
    time.sleep(time_delay)

    if curr_node == destination:
        nodes[curr_node][0] = color_visited
        nodes[curr_node][2] -= 10
        display_graph(screen,graph,nodes,edge_dict,num_sigla)
        time.sleep(time_delay)
        break


    former_neighbour_colors = []
    for neighbour_index, (neighbour_node, weight, edge_color) in enumerate(graph[curr_node]):
        # modifica cor do neighbour
        # this changes the rgb color of the edge from curr_node to neighbour_node
        edge_dict[tuple(sorted((curr_node, neighbour_node)))] = (color_current_edge, weight)
        # this saves the current color of the neighbour
        former_neighbour_colors.append(nodes[neighbour_node][0])
        # this changes its color to yellow, meaning the neighbour is been analyzed by the algorithm
        nodes[neighbour_node][0] = Yellow
        display_graph(screen,graph,nodes,edge_dict,num_sigla)
        pygame.display.flip()
        time.sleep(time_delay)

        # this relaxes the edge and puts it in the priority queue if necessary
        if cost[neighbour_node] > cost[curr_node] + weight:
            cost[neighbour_node] = weight + cost[curr_node] 
            parent[neighbour_node] = curr_node                # remember its parent in the shortest path tree
            pq.insert( (cost[neighbour_node], neighbour_node) )

    # this gives the neighbours their original color back
    for neighbour_index, (neighbour_node, _, _) in enumerate(graph[curr_node]):
        nodes[neighbour_node][0] = former_neighbour_colors[neighbour_index]
    
    nodes[curr_node][2] -= 10  # volta o node para o tamanho normal
    nodes[curr_node][0] = color_visited
# dijkstra terminated

# painting the shortest path to the source backwards
font = pygame.font.Font('freesansbold.ttf',number_size)
previous = destination
current = parent[destination]
while current is not None:
    pygame.draw.line(screen, Green, nodes[previous][1], nodes[current][1], 3)

    # drawing the nodes above the new lines
    pygame.draw.circle(screen, nodes[previous][0], nodes[previous][1], nodes[previous][2])
    text = font.render(num_sigla[previous],True,node_number_color)           # print node number            
    screen.blit(text,text.get_rect(center=nodes[previous][1]))  # print node number

    pygame.draw.circle(screen, nodes[current][0], nodes[current][1], nodes[current][2])
    text = font.render(num_sigla[current],True,node_number_color)           # print node number            
    screen.blit(text,text.get_rect(center=nodes[current][1]))         # print node number    

    pygame.display.flip()
    time.sleep(time_delay)

    previous = current
    current = parent[current]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                exit()
