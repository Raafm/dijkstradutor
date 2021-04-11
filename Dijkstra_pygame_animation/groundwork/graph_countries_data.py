initial_color =(255,255,255)
initial_raidus = 20

nodes = [
[initial_color , (582 ,   400) , initial_raidus],             # 'en'   node 0 
[initial_color , ( 350   ,  240  ) ,  initial_raidus  ],      # 'de'   node 1
[initial_color , ( 150   ,  370  ) ,  initial_raidus  ],      # 'it'   node 2
[initial_color , ( 600   ,  150  ) ,  initial_raidus  ],      # 'ru'   node 3
[initial_color , ( 250   ,  70  ) ,   initial_raidus  ],      # 'fr'   node 4
[initial_color , ( 820   , 480  ) ,   initial_raidus  ],      # 'zh'   node 5
[initial_color , ( 340   ,  550  ) , 1.5*initial_raidus],     # 'BR'   node 6    
[initial_color , ( 502   ,  70   ) , 1.5*initial_raidus],     # 'DE'   node 7    
[initial_color , ( 652   ,  240  ) , 1.5*initial_raidus],     # 'IN'   node 8    
[initial_color , ( 783   ,  150  ) , 1.5*initial_raidus],     # 'RU'   node 9    
[initial_color , ( 200   ,  200  ) , 1.5*initial_raidus],     # 'US'   node 10    
[initial_color , ( 800   ,  650  ) , 1.5*initial_raidus],     # 'AU'   node 11
[initial_color , ( 700   ,  370  ) , 1.5*initial_raidus]      # 'CN'   node 12
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
 [(6,0.96),(6, 0.08),(7, 0.64),(8,0.41),(10,0.96)]     ,    # 'en'   node 0                   
 [(6,0.008),(7, 0.91),(10, 0.005)]                     ,    # 'de'     node 1        
 [(6, 0.003),(7,0.07),(10,0.003)]                      ,    # 'it'    node 2 
 [(7,0.06),(9,0.94)]                                   ,    # 'ru'     node 3                         
 [(7,0.18 ),(10,0.006)]                                ,    # 'fr'     node 4     
 [(11,0.021),(12,0.9)]                                 ,    # 'zh'     node 5  
 [(1,0.008),(0, 0.08),(2, 0.003)]                      ,    # 'BR'     node 6         
 [(1, 0.91),(0,0.64),(4, 0.18),(2, 0.07), (3, 0.06)]   ,    # 'DE'     node 7 
 [(0, 0.19)]                                           ,    # IN     node 8                 
 [(3, 0.94) ]                                          ,    # 'RU'     node 9                                      
 [(1, 0.005),(0, 0.96),(4,0.006), (2, 0.003),  ]       ,    # 'US'    node 10
 [(0, 0.96 ),(5,0.021)]                                ,    # 'AU'     node 11   
 [(5, 0.9)]                                                 # 'CN'     node 12
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
    [5 , 12 , 0.9,inital_edge_color],
    [5 , 11 , 0.021,inital_edge_color]
] 
