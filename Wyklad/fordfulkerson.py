def DFS(G):

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

def FordFulkerson(G, s, t):

    #Wyszukuje sciezke powiekszajaca

    path = DFS(G)

    flow = 0

    while(path[t] != -1): #dopóki istnieje ścieżka powiększająca

        #teraz muszę znależć minimum w tej ścieżce powiększającej
        minVal = float('inf')
        curr = t

        while(curr != s):

            minVal = min(minVal, M[path[curr]][curr])
            curr = path[curr]
            #print(curr)

        #teraz muszę znależć minimum w tej ścieżce powiększającej
        curr = t
        while(curr != s):

            M[path[curr]][curr] -= minVal
            M[curr][path[curr]] += minVal
            curr = path[curr]

        flow += minVal

        path = DFS(G) #Wyszukuje sciezke powiekszajaca

    return flow



def ListToMatrixRepresentation( G ):

    M = [ [0 for j in range(len(G))] for i in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[i])):
            M[i][G[i][j][0]] = G[i][j][1]
            M[G[i][j][0]][i] = 0

    return M


G = [

    [(1,6), (4,3)],
    [(2,2), (4,1), (5,2)],
    [(3,4)],
    [],
    [(2,2), (5,1)],
    [(2,2), (3,4)]


]

M = ListToMatrixRepresentation(G)

print(FordFulkerson(M, 0, 3))
