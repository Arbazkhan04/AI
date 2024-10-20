from Graph import Graph, Node, Edge

def read_graph_from_file(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        lines = file.readlines()
        nodes_section = False
        edges_section = False

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith("graph"):
                graph_name = line.split()[1]
                nodes_section = False
                edges_section = False

            elif line.startswith("nodes"):
                nodes_section = True
                edges_section = False
                
            elif line.startswith("edges"):
                nodes_section = False
                edges_section = True

            elif nodes_section:
                nodes = line.split()
                for node in nodes:
                    graph.add_node(node)

            elif edges_section:
                parts = line.split()
                if len(parts) == 2:
                    state_from, state_to = parts
                    graph.add_edge(state_from, 'edge', 1, state_to)
                elif len(parts) == 3:
                    state_from, state_to, cost = parts
                    graph.add_edge(state_from, 'edge', int(cost), state_to)
    return graph



class TransportationProblem:
    def __init__(self, N):
        self.N = N
        self.graph = Graph()
        self._build_graph()

    def _build_graph(self):
        for state in range(1, self.N + 1):
            self.graph.add_node(state)
            if state + 1 <= self.N:
                self.graph.add_edge(state, 'walk', 1, state + 1)
            if state * 2 <= self.N:
                self.graph.add_edge(state, 'tram', 2, state * 2)
    
    def start_state(self):
        return 1
    
    def is_end(self, state):
        return state == self.N
    
    def successors(self, state):
        node = self.graph.get_node(state)
        return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]
    




class GridWorldProblem:
    def __init__(self, grid):
        self.grid = grid
        self.graph = Graph()
        self._build_graph()

    def _build_graph(self):
        rows = len(self.grid)
        cols = len(self.grid[0])

        for row in range(rows):
            for col in range(cols):
                state = (row, col)
                self.graph.add_node(state)
                if row + 1 < rows and self.grid[row + 1][col] != 0:
                    self.graph.add_edge(state, 'down', 1, (row + 1, col))
                if col + 1 < cols and self.grid[row][col + 1] != 0:
                    self.graph.add_edge(state, 'right', 1, (row, col + 1))
                if row - 1 >= 0 and self.grid[row - 1][col] != 0:
                    self.graph.add_edge(state, 'up', 1, (row - 1, col))
                if col - 1 >= 0 and self.grid[row][col - 1] != 0:
                    self.graph.add_edge(state, 'left', 1, (row, col - 1))
    
    def start_state(self):
        return (0, 0)
    
    def is_end(self, state):
        return state == (len(self.grid) - 1, len(self.grid[0]) - 1)
    
    def successors(self, state):
        node = self.graph.get_node(state)
        return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]
    



if __name__ == "__main__":

    # # Example usage
    # filename = "file.txt" # Replace with the path to your file
    # graph = read_graph_from_file(filename)

    # Example of initializing and getting successors for state 3
    # problem = TransportationProblem(N=10)
    # print(problem.successors(3)) 
    # problem.graph.print_graph()

        
    # grid = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    # problem = GridWorldProblem(grid)
    # print(problem.successors((0, 0)))  # [('right', (0, 1), 1)]

    pass
