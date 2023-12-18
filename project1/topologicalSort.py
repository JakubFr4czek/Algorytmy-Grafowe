#Listowo: O(E + V)

def DFS(G):

    def DFSVisit(G, v):

        nonlocal time
        time += 1

        visited[v] = True

        #print("v: ",v," czas: ", time)

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                path[G[v][i]] = v
                DFSVisit(G,G[v][i])

        time += 1 #Tak jakos lepiej to liczy jak jest zakomentowane
        print(v, end=' ')


    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]

    time = 0 #czas przetworzenia wierzcholka

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)

    #print(path)
