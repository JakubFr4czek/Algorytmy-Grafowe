from dimacs import *
from collections import deque
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

def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    Ni = set()
    Nj = set()

    for i in range(n-1):
        for j in range(i+1, n-1):
      
            for k in range(len(G[vs[i]])):
                Ni.add(G[vs[i]][k])

            for k in range(len(G[vs[j]])):
                Nj.add(G[vs[j]][k])

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts:
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min(verts) <= min(viable):
                    return False
    return True


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
#Graphs.append(directory + "cycle6")

for str in Graphs:

    V, L = loadWeightedGraph(str)

    G = listify(V, L)

    result = lexBFS(G, 0)

    #print("Rozwiazanie dla ", str, ": ", result)
    
    print(result)
    
    x = checkLexBFS(G, result)
    
    if x:
        trues += 1
        print("Zgodne ze wzrorcowym rozwiązaniem")
    else:
        falses += 1
        print("Niezgodne ze wzorcowym rozwiązaniem! Jest: ", result, ", powinno być: ", x)

    print("")
    

print("Zaliczone testy: ", trues)
print("Niezaliczone testy: ", falses)