from dimacs import *
import os

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

def perfectEliminationOrder(G, lex):

    RN_parent = [set() for i in range(len(lex))]

    for j in range(len(lex)):

        #Liczę zbiór RN(v), gdzie RN - wierzchołki sąsadujące z v, występujące przed nim w zbiorze lex
        neighbours = set()
        for i in range(len(G[lex[j]])):
            neighbours.add(G[lex[j]][i])

        predecessors = set()
        for i in range(0, j):
            predecessors.add(lex[i])

        RN_v = predecessors & neighbours

        #print(predecessors)
        #print(neighbours)

        if RN_v:

            #Wyznaczm parent
            for i in range(j - 1, -1, -1):

                if(lex[i] in RN_v):
                    parent_v = lex[i]
                    break

            parent_v_set = set()
            parent_v_set.add(parent_v)

            RN_v_no_parent = RN_v - parent_v_set

            #Debug
            #print(lex[j], RN_v, parent_v, parent_v_set, RN_v_no_parent, RN_parent[parent_v], RN_v_no_parent.issubset(RN_parent[parent_v]))

            if RN_v_no_parent.issubset(RN_parent[parent_v]) == False:
                return 0


        RN_parent[lex[j]] = RN_v

    return 1


Graphs = []
directory = "graphs-lab4/chordal/"

# iterate over files in 
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        Graphs.append(filename.path)

trues = 0
falses = 0

#Graphs = []
#Graphs.append(directory + "simple-noninterval2")

for str in Graphs:

    V, L = loadWeightedGraph(str)

    G = listify(V, L)

    lex = lexBFS(G, 0)

    print(lex)

    result = perfectEliminationOrder(G, lex)

    print("Rozwiazanie dla ", str, ": ", result)

    x = readSolution(str)
    x = int(x)
   
    if result == x:
        trues += 1
        print("Zgodne ze wzrorcowym rozwiązaniem")
    else:
        falses += 1
        print("Niezgodne ze wzorcowym rozwiązaniem! Jest: ", result, ", powinno być: ", x)

    print("")

print("Zaliczone testy: ", trues)
print("Niezaliczone testy: ", falses)