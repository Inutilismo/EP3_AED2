class PrintaGrafo:

    #mostra a quantidade de nós em cada lista de adjacentes
    def quantidadeNos(self): 
        quantidade = []
        for node in self.nodes:
            quantidade.append(len(self.adj[node]))
        return quantidade 

    #cria aresta entre dois vertices
    def add_edge(self, u, v): 
        self.adj[u].append(v)
        self.adj[v].append(u)
        
    #onstrutor do vetor de adjacentes
    def __init__(self, V):
        self.V = V 
        self.adj = [[] for i in range(V)]

    #mostra os vertices e seus adjacentes
    def print_adj_list (self): 
        for node in self.nodes:
            print (node, '->', self.adj[node])

    

    #busca em profundidade
    def DFSUtil(self, temp, v, visited): 
  
        #Marca o vértice que foi visitado
        visited[v] = True
  
        #Salva na lista
        temp.append(v) 
      
        #Guarda o caminho feito
        visitados = []
        visitados.append(v)

        #Repete o processo para todos os vértices adjacentes
        while (len(visitados) != 0):
            for i in self.adj[visitados[len(visitados)-1]]:             
                if visited[i] == False:
                    visitados.append(i)
                    visited[i] = True
                    temp.append(i)
            del(visitados[len(visitados)-1])
        
        return temp

    #Atualiza os componentes conexos
    def connectedComponents(self): 
        #vértices visitados e componentes conexos
        visited = [] 
        cc = []

        #inicializa o vetor de visitados
        for i in range(self.V): 
            visited.append(False) 

        #Para cada vértice não visitado, chama a função de busca em profundidade
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 