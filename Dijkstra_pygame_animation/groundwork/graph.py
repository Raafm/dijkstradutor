from .colors import White, Cyan, Gray

initial_node_color = White
initial_edge_color = Cyan
initial_radius = 20

nodes = [
    [ initial_node_color , ( 50  , 50   ), initial_radius ],         # Node 0
    [ initial_node_color , ( 160 , 100  ), initial_radius ],         # Node 1       
    [ initial_node_color , ( 80  , 350  ), initial_radius ],         # Node 2      
    [ initial_node_color , ( 170 , 300  ), initial_radius ],         # Node 3        
    [ initial_node_color , ( 180 , 550  ), initial_radius ],         # Node 4
    [ initial_node_color , ( 320 , 370  ), initial_radius ],         # Node 5      
    [ initial_node_color , ( 320 , 500  ), initial_radius ],         # Node 6
    [ initial_node_color , ( 350 , 100  ), initial_radius ],         # Node 7      
    [ initial_node_color , ( 450 , 550  ), initial_radius ],         # Node 8
    [ initial_node_color , ( 630 , 100  ), initial_radius ],         # Node 9
    [ initial_node_color , ( 460 , 385  ), initial_radius ],         # Node 10
    [ initial_node_color , ( 650 , 350  ), initial_radius ],         # Node 11
    [ initial_node_color , ( 750 , 550  ), initial_radius ],         # Node 12
]

# node 1, node 2, peso, cor
edge_list = [
    [ 0 , 1  , 100, initial_edge_color ],  
    [ 0 , 2  , 200, initial_edge_color ],
    [ 1 , 2  , 100, initial_edge_color ],
    [ 1 , 3  , 300, initial_edge_color ],
    [ 2 , 3  , 300, initial_edge_color ],
    [ 2 , 4  , 400, initial_edge_color ],
    [ 3 , 5  , 200, initial_edge_color ],
    [ 3 , 7  , 600, initial_edge_color ],
    [ 4 , 5  , 200, initial_edge_color ],
    [ 4 , 6  , 400, initial_edge_color ],
    [ 4 , 8  , 200, initial_edge_color ],
    [ 5 , 6  , 400, initial_edge_color ],
    [ 5 , 7  , 300, initial_edge_color ],
    [ 5 , 10 , 400, initial_edge_color ],
    [ 6 , 10 , 200, initial_edge_color ],
    [ 7 , 11 , 300, initial_edge_color ],
    [ 8 , 10 , 200, initial_edge_color ],
    [ 9 , 11 , 400, initial_edge_color ],
    [ 10, 11 , 300, initial_edge_color ],
    [ 10, 12 , 500, initial_edge_color ],
    [ 11, 12 , 200, initial_edge_color ]
]


test_graph = []
for _ in range(len(nodes)):  # len(nodes) == 13
    test_graph.append([])

for node_u, node_v, weight, edge_color in edge_list:
    
    test_graph[node_u].append( [node_v , weight , edge_color] )
    test_graph[node_v].append( [node_u , weight , edge_color] )
    
# print(test_graph)

# test_graph: lista de nodes
# test_graph[i] == lista de adjacencia
# cada elemento da lista de adjacencia:  [node vizinho, peso_aresta, color_tuple_ARESTA]

# esse eh o grafo printado na linha 58
test_graph = [
    [
     [1, 100, Gray],
     [2, 200, Gray]
    ],

    [
     [0, 100, Gray],
     [2, 100, Gray],
     [3, 300, Gray]
    ],

    [
     [0, 200, Gray],
     [1, 100, Gray],
     [3, 300, Gray],
     [4, 400, Gray]
    ],

    [
     [1, 300, Gray],
     [2, 300, Gray],
     [5, 200, Gray],
     [7, 600, Gray]
    ],

    [
     [2, 400, Gray],
     [5, 200, Gray],
     [6, 400, Gray],
     [8, 200, Gray]
    ],

    [
     [3, 200, Gray],
     [4, 200,Gray],
     [6, 400, Gray],
     [7, 300, Gray],
     [10, 400, Gray]
    ],

    [
     [4, 400, Gray],
     [5, 400, Gray],
     [10, 200, Gray]
    ],

    [
     [3, 600, Gray],
     [5, 300, Gray],
     [11, 300, Gray]
    ],

    [
     [4, 200, Gray],
     [10, 200, Gray]
    ],

    [
     [11, 400, Gray]
    ],

    [
     [5, 400, Gray],
     [6, 200, Gray],
     [8, 200, Gray],
     [11, 300, Gray],
     [12, 500, Gray]
    ],

    [
     [7, 300, Gray],
     [9, 400, Gray],
     [10, 300, Gray],
     [12, 200, Gray]
    ],

    [
     [10, 500, Gray],
     [11, 200, Gray]
    ]
]

edge_dict = {(0, 1): (White, 100), (0, 2): (White, 200), (1, 2): (White, 100), (1, 3): (White, 300), (2, 3): (White, 300), (2, 4): (White, 400), (3, 5): (White, 200), (3, 7): (White, 600), (4, 5): (White, 200), (4, 6): (White, 400), (4, 8): (White, 200), (5, 6): (White, 400), (5, 7): (White, 300), (5, 10): (White, 400), (6, 10): (White, 200), (7, 11): (White, 300), (8, 10): (White, 200), (9, 11): (White, 400), (10, 11): (White, 300), (10, 12): (White, 500), (11, 12): (White, 200)}
