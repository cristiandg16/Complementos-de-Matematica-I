def dijkstra(self):
    nodes = list(self.graph.nodes)
 
    for i in nodes: #Set first values
        dict_i = {}
        for j in nodes:
            if i == j:
                dict_i[j] = 0
            else:
                dict_i[j] = float("inf")
        self.distances[i] = dict_i
 
    for oneNode in nodes: #Start algoritm
        Q = []
        for node in nodes: Q.append(node)
 
        while len(Q) != 0:
            v = 0
            min = float("inf")
            for node_q in Q:
                if self.distances[oneNode][node_q] <= min:
                    min = self.distances[oneNode][node_q]
                    v = node_q
 
            Q.remove(v)
 
            neighbors = list(self.graph.neighbors(v))
 
            for neighborV in neighbors:
                w = self.graph[v][neighborV]['weight']
                alt = self.distances[oneNode][v] + w
                if alt < self.distances[oneNode][neighborV]:
                    self.distances[oneNode][neighborV] = alt
 
    return self.distances
