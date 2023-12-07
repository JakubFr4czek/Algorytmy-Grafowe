from dimacs import *
from collections import deque
import os
#Listowo: O(E + V)

def lexBFS(G, v):

    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]

    #elementy lexBFS
    lista = []
    lista.append({i for i in range(1, len(G))})
    lista.append({0})

    res = []

    while len(lista) > 0:
        
        #print( lista)

        temp = lista[-1].pop()

        #print(temp)

        visited[temp] = True

        res.append(temp)

        #print(lista[-1])

        nowaLista = []

        #Tworzę zbiór dzieci, które mogę odwiedzić
        A = set()
        for i in range(len(G[temp])):
            if visited[G[temp][i]] == False:
                A.add(G[temp][i])

        for i in range(len(lista)):
            #Usuwam część wspólną
            nowaLista.append(lista[i] - A)
            nowaLista.append(lista[i] & A)
                
        #lista.insert(A)

        lista = list(filter(lambda a : len(a) > 0, nowaLista))
        
    return res


def listify(V, L):

    G = [[] for _ in range(V)]

    for v1, v2, w in L:

        G[v1 - 1].append( (v2 - 1) )
        G[v2 - 1].append( (v1 - 1) )
    return G

def getNeighbours(G, v):

    neighbours = []

    for i in range(len(G[v])):

        neighbours.append(G[v][i])

    return neighbours

def getNeighboursColors(G, neighbours, colors):

    neighboursColors = set()

    for n in neighbours:

        neighboursColors.add(colors[n])

    return neighboursColors

def colorGraph(G, lex):

    colors = [0 for _ in range(len(lex))]

    usedColors = set()

    for v in lex:

        neighbours = getNeighbours(G, v)
        neighboursColors = getNeighboursColors(G, neighbours, colors)
        nextColor = 0

        notUsed = list(usedColors - neighboursColors)
        
        if(len(notUsed) > 0):
            nextColor = notUsed[0]

        if nextColor == 0 and len(usedColors) == 0:
            nextColor = 1
        elif nextColor == 0 and len(usedColors) > 0:
            nextColor = list(usedColors)[-1] + 1


        colors[v] = nextColor
        usedColors.add(nextColor)

    return max(colors)


Graphs = []
directory = "graphs-lab4/coloring/"

# iterate over files in 
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        Graphs.append(filename.path)

trues = 0
falses = 0

#Graphs = []
#Graphs.append(directory + "cycle6")

for str in Graphs:

    if str == directory + ".path.swp":
        continue

    V, L = loadWeightedGraph(str)

    G = listify(V, L)

    lex = lexBFS(G, 0)

    result = colorGraph(G, lex)

    
    x = readSolution(str)
    
    if int(x) == result:
        trues += 1
        print("Zgodne ze wzrorcowym rozwiązaniem")
    else:
        falses += 1
        print("Niezgodne ze wzorcowym rozwiązaniem! Jest: ", result, ", powinno być: ", x)

    print("")
    

print("Zaliczone testy: ", trues)
print("Niezaliczone testy: ", falses)