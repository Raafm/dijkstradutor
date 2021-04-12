# Local application imports only
# adj is the adjacency list of the graph that represents the database
# (it can be found on dijkstradutor/Database)
from data_treatment.adjacency import adj
from data_treatment.names_initials.data_relations.data_relations import initials_name, num_initials, initials_num, num_coordinates
from Dijkstra_pygame_animation.groundwork.heap import Heap
import folium

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
    # handling destination integer input
    while True:
        try:
            destination = int(input("Destination country (in range [615, 868]): "))  # an integer from 615 to 868
            if destination < 615 or destination > 868:
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
    # handling destination string input
    while True:
        try:
            destination = initials_num[input("Destination country: ")]
            break
        except KeyError:
            print("These initials are not in the database! Please try again. (Hint: use capital letters and/or try finding a shorter country code")
print()  # new line

# this defines a min priority queue (pq) of pairs for use in the Dijkstra.
# The pairs used will be of the form (distance_from_source, vertex).
pq = Heap(comp=lambda tuple1, tuple2: tuple1[0] > tuple1[1])
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
    if vertex == destination:
        break
    # if vertex >= 615, then 'vertex'it is a country, and its neighbours are languages.
    # Otherwise, it is a lang, and its neighbours are countries.
    for neighbour, weight in adj[vertex]:  # adjacent vertex, edge weight
        if dist[neighbour] > dist[vertex] + weight: # weight is 0 if neighbour is a country
            dist[neighbour] = dist[vertex] + weight
            path[neighbour] = vertex
            pq.insert( (dist[neighbour], neighbour) )
# dijkstra terminated

# saving the path from source to destination in a single array for outputting
path_list = []
current = destination
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
source_int = source
source = num_initials[source]  # transforming number into the associated initials
try:
    source = initials_name[source]
except KeyError:
    pass

destiny_num = destination
destination = num_initials[destination]  # getting the initials which correspond to destination
try:
    destination = initials_name[destination]
except KeyError:
    pass

print(f"The least distance from {source} to {destination} is {dist[destiny_num]}, which corresponds to this path:")
print(path_string[:-4])

# folium part down here
def median_pais(coordinate1,coordinate2):
    media =list()
    media.append(  (coordinate1[0] + coordinate2[0])/2  )
    media.append( (coordinate1[1] + coordinate2[1])/2 )
    return media

m = folium.Map(location=[0,0], zoom_start=2)

pais_envia = []
pais_envia.append(num_initials[path_list[-1]])
pais_envia.append(num_coordinates[path_list[-1]-615][0])
pais_envia.append(num_coordinates[path_list[-1]-615][1])
folium.Marker([pais_envia[1], pais_envia[2] ],weight=3, popup=initials_name[num_initials[source_int]]).add_to(m)
idioma = path_list[-2]
pais_recebe = None

#because we need to jump the first node in the for loop (wich is the source)
is_source = True
# indicates if current node in reversed(path_list) is an idiom or a country.
# As it is a bipartite graph, after a idiom we have a country
is_idioma = True
for element in reversed(path_list):
    
    if is_source:
        is_source = False
        continue
    
    if is_idioma:
        idioma = num_initials[element]
        
    else:    
        pais_recebe = [num_initials[element], num_coordinates[element-615][0], num_coordinates[element-615][1]]  
        
        loc = [(pais_envia[1], pais_envia[2]),
            (pais_recebe[1], pais_recebe[2])]

        coordinate1 = [ pais_envia[1] , pais_envia[2] ]
        coordinate2 = [ pais_recebe[1] , pais_recebe[2] ]
        
        text_popup = 'from: ' +  initials_name[pais_envia[0]] + '\nto: ' + initials_name[pais_recebe[0]] + '\nlang: ' + initials_name[idioma]
        
        # escrever em cima da linha que une os países
        folium.Marker(median_pais(coordinate1, coordinate2),weight=3, popup=text_popup, icon=folium.Icon(icon="envelope", color="red")).add_to(m)
        
        # drawline
        folium.PolyLine(loc, weight=3, color='blue').add_to(m)
        
        pais_envia = pais_recebe
        
    is_idioma = not is_idioma
    
m.save('coiso.html')  # mapa
    
    
