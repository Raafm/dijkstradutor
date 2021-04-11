import pygame

if __name__ == "__main__":
    from colors import *
else:
    from .colors import *

circle_color = White
line_color = Cyan
peso_color = Red
node_number_color = Red
text_color = Green
number_size = 12
radius = 7
screen_color = Teal

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf',number_size)

def display_graph(screen,graph,nodes,edge_dict,num_siglas):

    def show_weight(peso,position):
        text = font.render(str(peso),True,peso_color)
        screen.blit(text,position)

    def median_point(p1,p2):
        return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

    screen.fill(screen_color)

    node_counter = 0
    for adjacent_list_of_node in graph:
        for neighbour_node, weight, edge_color in adjacent_list_of_node:

            for edge in edge_dict: # draw edges
                n1, n2 = edge
                color, weight = edge_dict[edge]
                pygame.draw.line(screen, color, nodes[n1][1], nodes[n2][1], 3)

            #show       weight(cost) of edge, place at the meadian_point between our current nodes
            show_weight(weight, median_point( nodes[node_counter][1], nodes[neighbour_node][1] ))

        node_counter += 1

    node_counter = 0
    for adjacent_list_of_node in graph:

        # draw circul of current node:         color == [0] ,   position   ==    [1] ,         radius  =  [2]
        pygame.draw.circle( screen,  nodes[node_counter][0] , nodes[node_counter][1] , nodes[node_counter][2] )
        text = font.render(num_siglas[node_counter],True,node_number_color)           # print node number            
        screen.blit(text,text.get_rect(center=nodes[node_counter][1]))  # print node number
        node_counter += 1                                               # print node number
        
    pygame.display.flip()


# for testing purposes
if __name__ == "__main__":

    from graph import test_graph as graph
    from graph import nodes, edge_dict,num_siglas

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    display_graph(screen,graph,nodes,edge_dict,num_siglas)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    exit()
