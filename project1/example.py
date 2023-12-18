from data import runtests, runFirstTest
from mosty import Mosty
from floydWarshall import FloydWarshall
from collections import deque
from queue import PriorityQueue

def listify(V, L):

    G = [[] for _ in range(V)]

    for v1, v2, w in L:

        G[v1 - 1].append( ((v2 - 1), w) )
        G[v2 - 1].append( ((v1 - 1), w) )

    return G


def find_places(G, low):

    places = set()

    for v in range(len(G)):

        for i in range(len(G[v])):
            
            #len(G[v]) > 1 and 
            if len(G[v]) > 1 and low[v] != low[G[v][i][0]]:
                places.add(v)

    return places

#O(ElogV)

def Dijkstra(G, v):

    distance = [float('inf') for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    queue = PriorityQueue()

    distance[v] = 0
    queue.put((0, v))

    while not queue.empty():

        priotity, temp = queue.get()

        for i in range(len(G[temp])):

            if distance[G[temp][i][0]] > priotity + G[temp][i][1]:
                distance[G[temp][i][0]] = priotity + G[temp][i][1]
                path[G[temp][i][0]] = temp
                queue.put((distance[G[temp][i][0]], G[temp][i][0]))

    return distance

def BFS(G, places, leaves):

    newGraph = [[] for i in range(len(places))]
    graphVertices = set()
    
    for lv in leaves:
        
        visited = [False for _ in range(len(G))]

        queue = deque()
        queue.append(lv)

        visited[lv] = True

        while(len(queue) > 0):

            temp = queue.popleft()

            for i in range(len(G[temp])):

                if visited[G[temp][i][0]] == False:

                    visited[G[temp][i][0]] = True

                    if G[temp][i][0] in places:

                        dist  = Dijkstra(G, pl)

                        newGraph[pl].append( (G[temp][i][0], dist[G[temp][i][0]]) )
                        newGraph[G[temp][i][0]].append( (pl, dist[G[temp][i][0]]) )
                    else:
                        queue.append(G[temp][i][0])


    return newGraph





def my_solve(N, streets):

    #print(f"Place: {N}, ulice: {len(streets)}")
    

    #Najpierw zamienię na reprezentację listową
    G = listify(N, streets)

    #Id grafów, które powstana po usunieciu mostow
    low = Mosty(G)

    #place
    places = find_places(G, low)
    
    vertices = set([i for i in range(len(G))])

    #print(vertices)

    leaves = vertices - places

    distance, parent = FloydWarshall(G)

    leaves = list(leaves)

    paths = []

    for i in range(len(leaves)):

        for j in range(i + 1, len(leaves)):

            #Sprawdzam ścieżkę od liścia i-tego do j-tego
            
            #print(leaves[i], leaves[j])

            placesCnt = 0
            pathLength = distance[leaves[i]][leaves[j]]

            temp = leaves[j]

            while temp != leaves[i]:
                


                if temp in places:
                    placesCnt += 1

                temp = parent[leaves[i]][temp]

            if placesCnt > 0:
                paths.append((placesCnt, pathLength))

    paths = sorted(paths, key= lambda l : (l[0], l[1] * (-1)), reverse=True)
 
    #print(paths)

    if len(paths) > 0:

        return(paths[0])
    
    return (-1, -1)
    
            

    #for d in distance:
    #    print(d)

    #for p in parent:
    #    print(p)
    

    #print(places)
    #najkrótsza ścieżka między placami

    #print(places)

    #newGraph = BFS(G, places, leaves)

    #for x in newGraph:
    #    print(x)


    #Odpalam bfs w podgrafie dijkstra najkrotsza sciezka do kazdego placu

runtests(my_solve)


#runFirstTest(my_solve)
