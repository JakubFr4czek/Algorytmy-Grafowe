#Najkrotsze sciezki miedzy kazdym wierzcholkiem
#Zlozonosc obliczeniowa O(n^3)
#Zlozonosc pamieciowa O(n^2)


def FloydWarshall(G):

    #Przygotowanie macierzy

    distance = [ [float('inf') for j in range(len(G))] for i in range(len(G)) ]
    parent = [ [-1 for j in range(len(G))] for i in range(len(G)) ]

    #Wpisuje krawedzie do macierzy

    #Iteracja po pwszystkich krawedziach grafu O(E)
    for i in range(len(G)):
        for j in range(len(G[i])):
            distance[i][G[i][j][0]] = G[i][j][1]
            parent[i][G[i][j][0]] = i

    #Droga do samego siebie ustawiam na 0
    for i in range(len(distance)):
        distance[i][i] = 0
    
    #Skracanie Sciezek
    for i in range(len(distance)): #Chcemy to zrobic n-razy
        for j in range(len(distance)):
            for k in range(len(distance)):
                #if j != i and i != k: #Nie jestem pewny tego
                    if distance[j][i] + distance[i][k] < distance[j][k]:
                        distance[j][k] = distance[j][i] + distance[i][k]
                        parent[j][k] = parent[i][k]
                        

    return distance, parent
    

'''
G = [

    [(1,2), (2,4)],
    [(2,3), (3,3)],
    [(3,-1), (4,4)],
    [(4,2)],
    []

]

print(FloydWarshall( G ))
'''