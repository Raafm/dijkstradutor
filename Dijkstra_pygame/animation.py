import pygame,time
from add_edges import display_graph

from graph import test_graph as graph
from graph import nodes


from heap import MaxHeap                #MINHeap


# fiz um arquivo com as cores em rgb,
# podemos pegar de la as cores que formos usar.
# Mesmo se vc achar que nao vai usar, nao apague as outras cores,
#  pois talvez vc mude de ideia sobre as melhores cores para o node

Black	    =	    (0,0,0)
White	    =	    (255,255,255)
Red  	    =	    (255,0,0)
Yellow	    =	    (255,255,0)

color_unvisited = White         # se modificar esse tme que modificar no arquivo graph tambem, ou fazer funcao para  modificar aqui
color_visited   = Yellow	    
color_current = (190,190,190)     #modificar
current_edge_color = (255,255,255) #modificar


INFINITY = 1000000
time_delay = 1000                               #tempo referencia para o codigo parar apos atualizar a tela

pygame.init()                                   #nao sei pq aparece esse,mas ele roda mesmo assim

screen = pygame.display.set_mode((800,600))

display_graph(screen,graph,nodes)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    
  


    #dijkstra:

    source = int(input("Source: "))                                #    TRATAR ERROS DE INPUT
    destination = int(input("Destination: "))

    nodes[source][0] = Red

    display_graph(screen,graph,nodes)                              # display inicial da tela

    
    cost = list([INFINITY]*len(nodes))                             #  tratar erro do primeiro node ser 1 e nao 0
    cost[source] = 0

    parent = list(range(len(nodes)))                               #  tratar erro do primeiro node ser 1 e nao 0
    parent[source] = source
    
    pq = MaxHeap()
    pq.insert(source)

    while not pq.empty():
  
        current_node = pq.pop()

        if current_node != source:

            nodes[current_node][0] = color_current                                #indicamos a visita ao node
            nodes[current_node][2] += 5                                             # aumenta tamanho do node
        
     

        display_graph(screen,graph,nodes)                                           # atualiza tela
        time.sleep( time_delay )

        if current_node == destination:
            break
        
        counter_node = 0    #talvez seja melhor usar o enumarate(), mas meu sotaque de C nao deixa
        for  neighbour_node, weight, edge_color in graph[current_node]:
            #cmodificar cor do neighbour
            graph[current_node][counter_node][2] = current_edge_color
            display_graph(screen,graph, nodes)
            time.sleep( time_delay )

            if cost[current_node] < cost[neighbour_node] - weight :

                cost[neighbour_node] += weight + cost[current_node]             # relax node
                parent[neighbour_node] = current_node                           # remember his parent
                pq.insert(neighbour_node)#inserir key para comparacao, nao fiz  # insert neighbour in priority_queue             
            
            counter_node +=1
        nodes[current_node][2] -= 5                                             # volta o node para o tamanho normal

    