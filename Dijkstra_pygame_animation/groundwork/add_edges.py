import pygame
from graph import test_graph as graph
from graph import nodes


circle_color = (255,255,255)
line_color = (0,100,200)
peso_color = (220,0,0)
number_size = 12
radius = 7

pygame.init()
screen = pygame.display.set_mode((800,600))

screen.fill((0,0,0))

def display_graph(screen,graph,nodes):

    font = pygame.font.Font('freesansbold.ttf',number_size)

    def show_weight(peso,position):
        text = font.render(str(peso),True,peso_color)
        screen.blit(text,position)

    def median_point(p1,p2):
        return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

    
    node_counter =0
    for adjacent_list_of_node in graph:
        for neighbour_node, weight, edge_color  in adjacent_list_of_node:
            
            pygame.draw.line(screen,  edge_color , nodes[node_counter][1] , nodes[neighbour_node][1])

            #show       weight(cost) of edge, place at the meadian_point between our current nodes
            show_weight( weight ,      median_point( nodes[node_counter][1]    ,   nodes[neighbour_node][1] )    ) 

        node_counter += 1

    node_counter = 0
    for adjacent_list_of_node in graph:

        #draw circul of current node:          color == [0] ,   position   ==    [1] ,         radius  =  [2]
        pygame.draw.circle( screen,  nodes[node_counter][0] , nodes[node_counter][1] , nodes[node_counter][2] )
        
        text = font.render(str(node_counter),True,(0,100,50))   #print node number            
        screen.blit(text,nodes[node_counter][1])                #print node number
        node_counter += 1                                       #print node number
        
    pygame.display.update()









    
if __name__ == "__main__":
    display_graph(screen,graph,nodes)


    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
    
    
