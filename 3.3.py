from dimacs import *
import copy

#Algorytm poprawny
#Fenomenalnie wytłumaczony w tym filmie: https://www.youtube.com/watch?v=AtkEpr7dsW4&ab_channel=MoguStew

#Jedynie grid100x100 się długo wykonuje

#Miejsce na optymalizacje jest w tej funkcji, teraz wyszukuje za każdym razem największą krawędź, a można
#by to jakoś inaczej spróbować załatwić
def findMaxEdge(G, v):

    maxEdge = -1
    maxEdgeValue = 0

    for i in range(len(G[v])):

        if G[v][i] > maxEdgeValue:
            maxEdgeValue = G[v][i]
            maxEdge = i

    return maxEdge, maxEdgeValue

def concatVertices(G, s, t):

    #Dodaję krawędzie z t do s

    for i in range(len(G[s])):

        G[t][i] += G[s][i]
        G[s][i] = 0

        G[i][t] += G[i][s]
        G[i][s] = 0 

    G[t][t] = 0
    G[t][s] = 0


def findCut(G):

    lastVal = float('inf')
    lastVertices = (-1, -1)

    s = 0    

    #Szukam największej krawędzi
    t, eVal = findMaxEdge(G, 0)
    
    '''
    for x in G:
        print(x)

    print()
    '''

    if t != -1:
        lastVal = eVal
        lastVertices = (s, t)


    while t != -1:

        #Łączę s z t
        concatVertices(G, s, t)

        s = t
        t, eVal = findMaxEdge(G, s)

        '''for x in G:
            print(x)

        print()
        '''
        

        #print(s, t)

        if t != -1:
            lastVal = eVal
            lastVertices = (s, t)
        
    return lastVal, lastVertices





'''def Listify(V, L):

    G = [[] for _ in range(V)]

    for v1, v2, w in L:

        G[v1 - 1].append((v2 - 1, w))
        print(v2 - 1)
        G[v2 - 1].append((v1 - 1, w))

    return G
'''

def MatrixifyNotDirected(V, L):
    
    M = [ [0 for j in range(V)] for i in range(V)]

    for v1, v2, w in L:
        M[v1 - 1][v2 - 1] = w
        M[v2 - 1][v1 - 1] = w

    return M 

def Stoer_Wagner(G):

    minCut = float('inf')

    cut, (s, t) = findCut(copy.deepcopy(G))
    concatVertices(G, s, t)
    minCut = min(minCut, cut)

    while cut != float('inf'):

        cut, (s, t) = findCut(copy.deepcopy(G))
        concatVertices(G, s, t)
        minCut = min(minCut, cut)

    return minCut


path = "C:\\Users\\48667\\Documents\\AGH UST\\Algorytmy-Grafowe\\graphs-lab3\\"

Graphs = ["clique5", "clique20", "clique100", "clique200", "cycle", "geo20_2b", "geo20_2c", "geo100_2a", "grid5x5", "mc1", "mc2", "path", "rand20_100", "rand100_500", "simple", "trivial", "grid100x100",]

trues = 0
falses = 0

for str in Graphs:

    V, L = loadWeightedGraph(path + str)

    M = MatrixifyNotDirected(V, L)

    result = Stoer_Wagner(M)

    print("Rozwiazanie dla ", str, ": ", result)
    

    x = readSolution(path + str)
    
    if result == int(x):
        trues += 1
        print("Zgodne ze wzrorcowym rozwiązaniem")
    else:
        falses += 1
        print("Niezgodne ze wzorcowym rozwiązaniem! Jest: ", result, ", powinno być: ", x)

    print("")

print("Zaliczone testy: ", trues)
print("Niezaliczone testy: ", falses)