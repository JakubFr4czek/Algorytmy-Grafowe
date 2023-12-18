def DFS(G, dist, low):

    def DFSVisit(G, v, parent):

        nonlocal dystans
        dist[v] = dystans
        dystans += 1

        visited[v] = True

        dziecko_w_dfs = -1 #jedyne dziecko w dfs

        for i in range(len(G[v])):

            if visited[G[v][i][0]] == False:
                dziecko_w_dfs = G[v][i][0]
                DFSVisit(G,G[v][i][0], v)

        #Wierzcholek przetworzony

        low[v] = dist[v]

        if dziecko_w_dfs != -1:
            low[v] = min(low[v], low[dziecko_w_dfs])

        for i in range(len(G[v])):
            if G[v][i][0] != parent and G[v][i][0] != dziecko_w_dfs:   
                    low[v] = min(low[v], dist[G[v][i][0]])

        #if low[v] == dist[v] and parent != -1:
        #    print(v, parent)


    visited = [False for _ in range(len(G))]
    dystans = 1

    for i in range(len(G)):

        if G[i] != [] and visited[i] == False:
            DFSVisit(G, i, -1)

def Mosty( G ):

    dist = [float('inf')] * len(G)
    low = [float('inf')] * len(G)

    DFS(G, dist, low)

    return low

'''
G = [

    [1,6],  #0
    [0,2],  #1
    [1,3,6],#2
    [2,4,5],#3
    [3,5],  #4
    [3,4],  #5
    [0,2,7],#6
    [6]     #7

]

low = Mosty( G )
'''
