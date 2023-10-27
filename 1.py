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

#V, L = loadWeightedGraph("/home/jakubfraczek/Dokumenty/AlgorytmyGrafowe/graphs-lab1/g1")
V, L = loadWeightedGraph("C:\\Users\\48667\\Documents\\AGH UST\\Algorytmy-Grafowe\\graphs-lab1\\g1")

s = 1
t = 2

result = maxMinWeight(L, V, s, t)

print(result)

#x = readSolution("/home/jakubfraczek/Dokumenty/AlgorytmyGrafowe/graphs-lab1/g1")
x = readSolution("C:\\Users\\48667\\Documents\\AGH UST\\Algorytmy-Grafowe\\graphs-lab1\\g1")
