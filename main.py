from Create_graph.adjacency import adj
from Create_graph.Nodes.data_relations.data_relations import initials_name, num_initials, initials_num
from heap import MaxHeap

N = 868  # number of vertices. They are numbered 1 through N+1

# handling cmd input
while True:
    try:
        cmd = int(input("0 for inputing numbers, 1 for inputing initials: "))
        if cmd != 0 and cmd != 1:
            print("The number must be either 0 or 1! Please try again.")
            continue
        break
    except ValueError:
        print("This is not a number! Please try again.")
print()  # new line
if cmd == 0:  # integer inputs
    # handling src integer input
    while True:
        try:
            src = int(input("Source country (in range [615, 868]): "))  # an integer from 615 to 868
            if src < 615 or src > 868:
                print("Number out of range! Try again.")
                continue
            break
        except ValueError:
            print("This is not a number! Please try again.")
    print()
    # handling dest integer input
    while True:
        try:
            dest = int(input("Destination country (in range [615, 868]): "))  # an integer from 615 to 868
            if dest < 615 or dest > 868:
                print("Number out of range! Try again.")
                continue
            break
        except ValueError:
            print("This is not a number! Please try again.")
else:  # string inputs
    # handling src string input
    while True:
        try:
            src = initials_num[input("Source country: ")]
            break
        except KeyError:
            print("These initials are not in the database! Please try again. (Hint: use capital letters and/or try finding a shorter country code")
    print()
    # handling dest string input
    while True:
        try:
            dest = initials_num[input("Destination country: ")]
            break
        except KeyError:
            print("These initials are not in the database! Please try again. (Hint: use capital letters and/or try finding a shorter country code")
print()

# min priority queue of pairs
pq = MaxHeap(comp=lambda tuple1, tuple2: tuple1[0] > tuple1[1])
pq.insert( (0, src) )

# distances from src. There are 1255 edges in the database and each
# has weight at most 1, so 1300 can be safely taken as infinity.
dist = [1300]*(N+1)
dist[src] = 0

# paths of minimum distances from the source
path = [None]*(N+1)

# running dijkstra
while not pq.empty():
    d, u = pq.pop()  # distance to source, vertex
    if d > dist[u]:
        continue
    if u == dest:
        break
    # if u >= 615, then 'u' is a country, and its neighbours are languages.
    # Otherwise, it is a lang, and its neighbours are countries.
    for v, w in adj[u]:  # adjacent vertex, edge weight
        if dist[v] > dist[u] + w: # w is 0 if v is a country
            dist[v] = dist[u] + w
            path[v] = u
            pq.insert( (dist[v], v) )

# saving the path from src to dest in a single array for outputting
path_list = []
current = dest
while current is not None:
	path_list.append(current)
	current = path[current]

# handling the path
path_string = ''
is_country = True
for u in reversed(path_list):
    u = num_initials[u]
    try:
        u = initials_name[u]
    except KeyError:
        pass
    if is_country:
        path_string += f"{u} country -> "
    else:
        path_string += f"{u} language -> "
    is_country = not is_country

# print handling
src = num_initials[src]  # transforming number into the associated initials
try:
    src = initials_name[src]
except KeyError:
    pass

dest_num = dest
dest = num_initials[dest]
try:
    dest = initials_name[dest]
except KeyError:
    pass

print(f"The least distance from {src} to {dest} is {dist[dest_num]}, which corresponds to this path:")
print(path_string[:-4])
