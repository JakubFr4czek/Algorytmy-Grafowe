import heapq
from dimacs import *

def findSet(parent, x):
    #Bo korzen sie zapetla do samego siebie
    if parent[x] != x:
        #kompresja sciezki
        parent[x] = findSet(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):

    x = findSet(parent, x)
    y = findSet(parent, y)

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y

        if rank[x] == rank[y]:
            rank[y] += 1

def maxMinWeight(G, V, s, t):
    
    G.sort(key = lambda x: x[2], reverse = True)

    parent = [i for i in range(V + 1)]
    rank = [0 for _ in range(V + 1)]

    result = float('inf')

    for (v1, v2, w) in G:

        #Wrzucam oba wierzcholki do zbioru
        union(parent, rank, v1, v2)

        result = min(result, w)

        #jesli s i t sa w zbiorze to mozna konczyc

        k1 = findSet(parent, s)
        k2 = findSet(parent, t)

        if k1 == k2:
            return result
        
    return None

Graphs = ["clique5", "clique20", "clique100", "clique1000", "g1", "grid5x5", "grid100x100", "path10", "path1000", "path10000", "pp10", "pp100", "pp1000", "rand20_100", "rand100_500", "rand1000_100000"]

falses = 0
trues = 0

for str in Graphs:

    #V, L = loadWeightedGraph("/home/jakubfraczek/Dokumenty/AlgorytmyGrafowe/graphs-lab1/g1")
    V, L = loadWeightedGraph("C:\\Users\\48667\\Documents\\AGH UST\\Algorytmy-Grafowe\\graphs-lab1\\" + str)

    s = 1
    t = 2

    result = maxMinWeight(L, V, s, t)

    print("Rozwiazanie dla ", str, ": ", result)

    #x = readSolution("/home/jakubfraczek/Dokumenty/AlgorytmyGrafowe/graphs-lab1/g1")
    x = readSolution("C:\\Users\\48667\\Documents\\AGH UST\\Algorytmy-Grafowe\\graphs-lab1\\" + str)

    if result == int(x):
        trues += 1
        print("Zgodne ze wzrorcowym rozwiązaniem")
    else:
        falses += 1
        print("Niezgodne ze wzorcowym rozwiązaniem! Jest: ", result, ", powinno być: ", x)

    print("")

print("Zaliczone testy: ", trues)
print("Niezaliczone testy: ", falses)

