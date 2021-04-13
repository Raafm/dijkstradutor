import pygame

if __name__ == "__main__":
    from colors import *
else:
    from .colors import *

circle_color = White
line_color = Cyan
peso_color = Black
node_number_color = Red
text_color = Green
number_size = 15
radius = 7
screen_color = Dark_gray

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf',number_size)
def display_graph(screen,graph,nodes,edge_dict,num_sigla):

    def show_weight(peso,position):
        text = font.render(str(peso),True,peso_color)
        screen.blit(text,position)

    def median_point(p1,p2):
        return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

    screen.fill(screen_color)

    node_counter = 0
    for edge in edge_dict:  # draw edges
        n1, n2 = edge
        color, weight = edge_dict[edge]
        pygame.draw.line(screen, color, nodes[n1][1], nodes[n2][1], 3)

    for adjacent_list_of_node in graph:
        for neighbour_node, weight, edge_color in adjacent_list_of_node:
            # show weight(cost) of edge, place at the meadian_point between our current nodes
            show_weight(weight, median_point(nodes[node_counter][1], nodes[neighbour_node][1]))
        node_counter += 1

    node_counter = 0
    for adjacent_list_of_node in graph:

        # draw circul of current node:         color == [0] ,   position   ==    [1] ,         radius  =  [2]
        pygame.draw.circle( screen,  nodes[node_counter][0] , nodes[node_counter][1] , nodes[node_counter][2] )
        text = font.render(num_sigla[node_counter],True,node_number_color)           # print node number            
        screen.blit(text,text.get_rect(center=nodes[node_counter][1]))  # print node number
        node_counter += 1                                               # print node number
        
    pygame.display.flip()


# for testing purposes
if __name__ == "__main__":

    # WARNING: before running this file, go to graph_countries_data.py and
    # erase the dot from the import statement. When you are done with
    # draw_graph.py (the current file), put the dot back, else main.py won't
    # work.

    from graph_countries_data import mini_graph as graph, nodes, edge_list, num_sigla, edge_dict

    pygame.init()
    screen = pygame.display.set_mode((900,700))
    display_graph(screen,graph,nodes,edge_dict,num_sigla)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    exit()
