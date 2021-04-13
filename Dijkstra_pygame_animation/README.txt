(Please open example.png for reference. In this example, Brazil
(BR) is the source vertex from which the algoirthm began)

Run main.py to observe Dijkstra's algorithm working in a simple

subgraph of the database. Univisted nodes are white; the current

node being visited, of which neighbours are analyzed, are green;

these analyzed nodes are yellow. Already visited nodes are blue

and edges that are part of some found shortest path are cyan.

When the algorithm finds the shortest path to the destination,

the edges that form the shortest path from the source to the des-

tination get green from the destination to the source, represen-

ting the structure of the "parent" vector that is used to save

the shortest path to all nodes from the source.