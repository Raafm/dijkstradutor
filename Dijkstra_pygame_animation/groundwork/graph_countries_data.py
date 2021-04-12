from .colors import White

initial_color =(255,255,255)
initial_raidus = 20

nodes = [
[initial_color , ( 582   ,  400) , initial_raidus],         # 'en'   node 0 
[initial_color , ( 400   ,  180) , initial_raidus],       # 'de'   node 1
[initial_color , ( 150   ,  370) , initial_raidus],       # 'it'   node 2
[initial_color , ( 600   ,  150) , initial_raidus],       # 'ru'   node 3
[initial_color , ( 250   ,  70 ) , initial_raidus],       # 'fr'   node 4
[initial_color , ( 820   ,  480) , initial_raidus],       # 'zh'   node 5
[initial_color , ( 340   ,  550) , 1.5*initial_raidus],     # 'BR'   node 6    
[initial_color , ( 502   ,  70 ) , 1.5*initial_raidus],     # 'DE'   node 7    
[initial_color , ( 652   ,  240) , 1.5*initial_raidus],     # 'IN'   node 8    
[initial_color , ( 783   ,  150) , 1.5*initial_raidus],     # 'RU'   node 9    
[initial_color , ( 200   ,  200) , 1.5*initial_raidus],     # 'US'   node 10    
[initial_color , ( 800   ,  650) , 1.5*initial_raidus],     # 'AU'   node 11
[initial_color , ( 700   ,  370) , 1.5*initial_raidus]      # 'CN'   node 12
]  

num_sigla = [
'en',    #english
'de',    #deutsch
'it',    #italian
'ru',    #russian
'fr',    #french
'zh',    #chinese
'BR',    #Brazil
'DE',    #Deutschland 
'IN',    #Indian
'RU',    #Russia
'US',    #United States
'AU',    #Australia
'CN'     #China
]

mini_graph = [
 [
     [6, 0.08 ,White],          # 'en'   node 0 
     [7, 0.64 ,White],
     [8,0.19 ,White],
     [10,0.96,White],
     [11,0.96, White]   
 ]  ,                     
 [
     [6,0.008 ,White],
     [7, 0.91 ,White],         # 'de'     node 1 
     [10, 0.005,White]                   
 ]  ,                          
 [
     [6, 0.003 ,White],         # 'it'    node 2 
     [10,0.003,White]                    
 ]  ,                    
 [                              # 'ru'     node 3  
     [7,0.06 ,White],
     [9,0.94,White]                                 
 ]  ,                                           
 [
     [7,0.18  ,White],         # 'fr'     node 4 
     [10,0.006,White]                              
 ]  ,                         
 [
     [11,0.021 ,White],        # 'zh'     node 5
     [12,0.9,White]                               
 ]  ,                        
 [ 
     [1,0.008 ,White],         # 'BR'     node 6 
     [0, 0.08 ,White],
     [2, 0.003,White]                    
 ]  ,                            
 [
     [1, 0.91 ,White],         # 'DE'     node 7
     [0,0.64 ,White],
     [4, 0.18 ,White],
     [3, 0.06,White] 
 ]  ,     
 [
     [0, 0.19,White]            # IN     node 8                                  
 ]  ,                                    
 [
     [3, 0.94,White]            # 'RU'     node 9                  
 ]  ,                                                            
 [
     [1, 0.005 ,White],        # 'US'    node 10
     [0, 0.96 ,White],
     [4,0.006 ,White],
     [2, 0.003,White]        
 ]  ,                    
 [
     [0, 0.96  ,White ],        # 'AU'     node 11
     [5,0.021,White]                              
 ]  ,                        
 [
     [5, 0.9,White]             # 'CN'     node 12            
 ]                             
]

inital_edge_color = (255,255,255)

edge_list= [
    [0 , 6  , 0.08  , inital_edge_color],
    [0 , 7  , 0.64  , inital_edge_color],
    [0 , 8  , 0.19  , inital_edge_color],
    [0 , 10 , 0.96  , inital_edge_color],
    [0 , 11 , 0.96  , inital_edge_color],
    [1 , 6  , 0.008 , inital_edge_color],
    [1 , 7  , 0.91  , inital_edge_color],
    [1 , 10 , 0.005 , inital_edge_color],
    [2 , 6  , 0.003 , inital_edge_color],
    [2 , 10 , 0.003 , inital_edge_color],    
    [3 , 7  , 0.06  , inital_edge_color],
    [3 , 9  , 0.94  , inital_edge_color],
    [4 , 7  , 0.18  , inital_edge_color],
    [4 , 10 , 0.006 , inital_edge_color], 
    [5 , 12 , 0.9   , inital_edge_color],
    [5 , 11 , 0.021 , inital_edge_color]
] 

edge_dict = {(0, 6): (White, 0.08), (0, 7): (White, 0.64), (0, 8): (White, 0.19), (0, 10): (White, 0.96), (0, 11): (White, 0.96), (1, 6): (White, 0.008), (1, 7): (White, 0.91), (1, 10): (White, 0.005), (2, 6): (White, 0.003), (2, 10): (White, 0.003), (3, 7): (White, 0.06), (3, 9): (White, 0.94), (4, 7): (White, 0.18), (4, 10): (White, 0.006), (5, 12): (White, 0.9), (5, 11): (White, 0.021)}
