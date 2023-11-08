from collections import deque
from dimacs import *

#Przechodzi wszystkie testy, ale ostatni się długo wykonuje


def DFS_old(G):

    def DFSVisit(G, v):

        visited[v] = True

        for i in range(len(G[v])):

            if G[v][i] != 0 and visited[i] == False:
                path[i] = v

                DFSVisit(G,i)


    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)

    return path

def DFS(M, s, t):

    visited = [False] * len(M)
    path = [-1 for _ in range(len(M))]

    stack = deque()

    visited[s] = True
    stack.append(s)

    while len(stack) > 0:

        temp = stack.pop()

        for i in range(len(M[temp])):

            if M[temp][i] != 0 and visited[i] == False:

                path[i] = temp

                if i == t:
                    return path
                
                visited[i] = True

                stack.append(i)

    return path
            

def fordFulkerson(M, s, t):

    flow = 0

    path = deque()
    path = DFS(M, s, t)

    while path[t] != -1:

        temp = t
        mini = float('inf')
    
        while temp != s:
            mini = min(mini, M[path[temp]][temp])
            temp = path[temp]

            if temp == - 1:
                break
        
        if temp != s:
            break

        temp = t

        while temp != s:
            M[path[temp]][temp] -= mini
            M[temp][path[temp]] += mini
            temp = path[temp]

        flow += mini
        path = DFS(M, s, t)

    return flow

        
def Matrixify(V, L):
    
    M = [ [0 for j in range(V)] for i in range(V)]

    for v1, v2, w in L:

        M[v1 - 1][v2 - 1] = w

    return M


path = "C:\\Users\\48667\\Documents\\AGH UST\\Algorytmy-Grafowe\\graphs-lab2\\flow\\"

Graphs = ["simple", "simple2", "clique5", "clique20", "clique100", "grid5x5", "pp100", "rand20_100", "rand100_500", "trivial", "trivial2", "worstcase", "grid100x100",]

#Graphs = ["grid100x100"]

trues = 0
falses = 0

for str in Graphs:


    V, L = loadDirectedWeightedGraph(path + str)

    M = Matrixify(V, L)

    result = fordFulkerson(M, 0, V - 1)

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