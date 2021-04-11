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
 [('AU',0.96),('BR', 0.08),('DE', 0.64),('IN',0.41),('US',0.96)]         ,    # 'en'     node 0                   
 [('BR',0.008),('DE', 0.91),('US', 0.005)]                               ,    # 'de'     node 1        
 [('BR', 0.003),('DE',0.07),('US',0.003)]                                ,    # 'it'     node 2 
 [('DE',0.06),('RU',0.94)]                                               ,    # 'ru'     node 3                         
 [('DE',0.18 ),('US',0.006)]                                             ,    # 'fr'     node 4     
 [('AU',0.021),('CN',0.9)]                                               ,    # 'zh'     node 5  
 [('de',0.008),('en', 0.08),('it', 0.003)]                               ,    # 'BR'     node 6         
 [('de', 0.91),('en',0.64),('fr', 0.18),('it', 0.07), ('ru' , 0.06)]     ,    # 'DE'     node 7 
 [('en', 0.19)]                                                          ,    # 'IN'     node 8                 
 [('ru', 0.94) ]                                                         ,    # 'RU'     node 9                                      
 [('de', 0.005),('en', 0.96),('fr',0.006), ('it', 0.003),  ]             ,    # 'US'     node 10
 [('en', 0.96 ),('zh',0.021)]                                            ,    # 'AU'     node 11   
 [('zh', 0.9)]                                                                # 'CN'     node 12
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
