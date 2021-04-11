from nodes import mini_graph as graph
from nodes import num_sigla,nodes,edge_list
import pygame 

color_circle = (255,255,255)
radius = 20

height = 700
width  = 950

def tela(latitude, longitude):
    x = ((width / 2)/180)*(longitude + 180) 
    y = ((height / 2 )/90)*( 90 - latitude )+ 250
    return (x,y)

def write(texto = "",position = (0,0),size = 10,cor = (100,0,0)):
    font = pygame.font.Font('freesansbold.ttf',size)
    text = font.render(texto,True,cor)
    screen.blit(text,position)

def draw_edges(screen,edge_list,num_sigla,nodes):

    for node1,node2, peso, color in edge_list:
        pygame.draw.line(screen,color,nodes[node1][1],nodes[node2][1],2)
        write(num_sigla[node1],nodes[node1][1],10,(100,0,100))
        write(num_sigla[node2],nodes[node2][1],10,(100,0,100))
        
pygame.init()

screen = pygame.display.set_mode((width,height))

draw_edges(screen,edge_list,num_sigla,nodes)

for n_node,(_,local,_) in enumerate(nodes):

    position = local
    
    pygame.draw.circle(screen,color_circle,position ,nodes[n_node][2])
    write(num_sigla[n_node],position)
    pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


