import heapq
from dimacs import *

def findSet(parent, x):
    #Bo korzen sie zapetla do samego siebie
    if parent[x] != x:
        #kompresja sciezki
        parent[x] = findSet(parent, parent[x])
    return parent[x]

def Union(parent, rank, x, y):

    x = findSet(parent, x)
    y = findSet(parent, y)

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y

        if rank[x] == rank[y]:
            rank[y] += 1

def Kurskal(G, V):
    
    for i in range(len(G)):
        G[i] = (-G[i][2], G[i][0], G[i][1])

    heap = []

    for i in range(len(G)):
        heapq.heappush(heap, G[i])
        #Sortuje w kolejnosci [0], [1], [2] jesli chodzi o krotke

    A = []
    parent = [i for i in range(V + 1)]
    rank = [0 for _ in range(V + 1)]

    while len(heap) > 0:
        
        temp = heapq.heappop(heap)

        k1 = findSet(parent, temp[1])
        k2 = findSet(parent, temp[2])

        if k1 != k2:
            A.append((temp[1], temp[2], -temp[0]))
            Union(parent, rank, temp[1], temp[2])
    return A






V, L = loadWeightedGraph("/home/jakubfraczek/Dokumenty/AlgorytmyGrafowe/graphs-lab1/g1")

#L[0] - a1
#L[1] - a1
#L[2] - w
print(L)
G = Kurskal(L, V)
print(G)

x = readSolution("/home/jakubfraczek/Dokumenty/AlgorytmyGrafowe/graphs-lab1/g1")
print(x)
#print(G)

#Znaleźć scieske z s (1) do t (2)