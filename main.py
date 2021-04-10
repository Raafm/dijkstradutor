# Local application imports only
# adj is the adjacency list of the graph that represents the database
# (it can be found on dijkstradutor/Database)
from Create_graph.adjacency import adj
from Create_graph.Nodes.data_relations.data_relations import initials_name, num_initials, initials_num
from heap import MaxHeap

N = 868  # number of vertices (languages + countries). They are numbere 1 through N+1

# handling command input
while True:
    try:
        command = int(input("0 for inputing numbers, 1 for inputing initials: "))
        if command != 0 and command != 1:
            print("The number must be either 0 or 1! Please try again.")
            continue
        break
    except ValueError:
        print("This is not a number! Please try again.")
print()  # new line
if command == 0:  # integer inputs
    # handling source integer input
    while True:
        try:
            source = int(input("Source country (in range [615, 868]): "))  # an integer from 615 to 868
            if source < 615 or source > 868:
                print("Number out of range! Try again.")
                continue
            break
        except ValueError:
            print("This is not a number! Please try again.")
    print()  # new line
    # handling destiny integer input
    while True:
        try:
            destiny = int(input("Destination country (in range [615, 868]): "))  # an integer from 615 to 868
            if destiny < 615 or destiny > 868:
                print("Number out of range! Try again.")
                continue
            break
        except ValueError:
            print("This is not a number! Please try again.")
else:  # string inputs
    # handling source string input
    while True:
        try:
            source = initials_num[input("Source country: ")]
            break
        except KeyError:
            print("These initials are not in the database! Please try again. (Hint: use capital letters and/or try finding a shorter country code")
    print()  # new line
    # handling destiny string input
    while True:
        try:
            destiny = initials_num[input("Destination country: ")]
            break
        except KeyError:
            print("These initials are not in the database! Please try again. (Hint: use capital letters and/or try finding a shorter country code")
print()  # new line

# this defines a min priority queue (pq) of pairs for use in the Dijkstra.
# The pairs used will be of the form (vertex, distance_from_source).
pq = MaxHeap(comp=lambda tuple1, tuple2: tuple1[0] > tuple1[1])
pq.insert( (0, source) )

# distances from source. There are 1255 edges in the database and each
# has weight at most 1, so 1300 can be safely taken as infinity.
dist = [1300]*(N+1)
dist[source] = 0

# paths of minimum distance from the source
path = [None]*(N+1)

# running dijkstra
while not pq.empty():
    dist_src, vertex = pq.pop()  # distance to source, vertex
    if dist_src > dist[vertex]:
        continue
    if vertex == destiny:
        break
    # if vertex >= 615, then 'vertex'it is a country, and its neighbours are languages.
    # Otherwise, it is a lang, and its neighbours are countries.
    for neighbour, weight in adj[vertex]:  # adjacent vertex, edge weight
        if dist[neighbour] > dist[vertex] + weight: # weight is 0 if neighbour is a country
            dist[neighbour] = dist[vertex] + weight
            path[neighbour] = vertex
            pq.insert( (dist[neighbour], neighbour) )
# dijkstra terminated

# saving the path from source to destiny in a single array for outputting
path_list = []
current = destiny
while current is not None:
    path_list.append(current)
    current = path[current]

# handling the path
path_string = ''
is_country = True
for vertex in reversed(path_list):
    vertex = num_initials[vertex]
    try:
        vertex = initials_name[vertex]
    except KeyError:
        pass
    if is_country:
        path_string += f"{vertex} country -> "
    else:
        path_string += f"{vertex} language -> "
    is_country = not is_country

# print handling
source = num_initials[source]  # transforming number into the associated initials
try:
    source = initials_name[source]
except KeyError:
    pass

destiny_num = destiny
destiny = num_initials[destiny]  # getting the initials which correspond to destiny
try:
    destiny = initials_name[destiny]
except KeyError:
    pass

print(f"The least distance from {source} to {destiny} is {dist[destiny_num]}, which corresponds to this path:")
print(path_string[:-4])
