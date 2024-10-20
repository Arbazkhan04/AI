class Graph:
    
    def __init__(self):
        self.is_directed = False
        self.vertices = []
        self.edges = []
        self.adj = {}

    def read_graph_from_file(self, filename):
        file = open(filename, 'r')
        data = file.readlines()
        self.vert = data[0].split('_')[0]
        self.is_directed = True if data[0].split('_')[1][0] == '1' else False
        self.vertices = data[1].split()
        self.edge = data[2]
        self.edges = [[source, dest] for i in range(3, len(data)) for source, dest in [data[i].split()]]
        file.close()
        self.form_graph()

    def get_vertex_count(self):
        return len(self.vertices)
    
    def get_edge_count(self):
        return len(self.edges)
    
    def is_graph_directed(self):
        return self.is_directed
    
    def get_neighbors(self, node):
        return self.adj[node]
    
    def form_graph(self):
        if self.is_directed == True:
            for source, dest in self.edges:
                self.adj.get(source, []).append(dest)
        else:
            for source, dest in self.edges:
                self.adj.get(source, []).append(dest)
                self.adj.get(dest, []).append(source)



               