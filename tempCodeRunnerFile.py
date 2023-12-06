def lexBFS(G, v):

    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]

    #elementy lexBFS
    lista = []
    lista.append({i for i in range(len(G))})

    res = []

    while len(lista) > 0:

        temp = lista[-1].pop()

        visited[temp] = True

        res.append(temp)

        #Tworzę zbiór dzieci, które mogę odwiedzić
        A = set()
        for i in range(len(G[temp])):
            if visited[G[temp][i]] == False:
                A.add(G[temp][i])

        for i in range(len(lista)):
            #Usuwam część wspólną
            lista[i] -= A
            
        lista.append(A)

        lista = list(filter(lambda a : len(a) > 0, lista))
        
    return res