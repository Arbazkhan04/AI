from Graph import Graph
from BestFirstSearch import BestFirstSearch, IterativeDeepeningSearch


class Puzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.graph = Graph()
        self.visited = set()
        #self._build_graph()

    def zero(self, state):
        for i, row in enumerate(state):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j


    def _build_graph(self):
        directions = [[1, 0, "down"], [0, 1, "right"], [-1, 0, "up"], [0, -1, "left"]]
        visited = set()
        frontier = [self.initial_state]
        self.graph.add_node(self.initial_state)

        while frontier:
            state = frontier.pop(0)
            if state in visited:
                continue
            
            visited.add(state)
            self.graph.add_node(state=state)

            for dr, dc, action in directions:
                r, c = self.zero(state)
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < 3 and 0 <= new_c < 3:   
                    new_state = [list(row) for row in state]
                    new_state[r][c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[r][c]
                    new_state = tuple(tuple(row) for row in new_state)

                    self.graph.add_edge(state, action, 1, new_state)
                    if new_state not in visited:
                        frontier.append(new_state)


    def start_state(self):
        return self.initial_state
    
    def is_end(self, state):
        return state == ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    
    def successors(self, state):
        # node = self.graph.get_node(state)
        # return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]

        directions = [[1, 0, "down"], [0, 1, "right"], [-1, 0, "up"], [0, -1, "left"]]
        r, c = self.zero(state)
        successors = []

        for dr, dc, action in directions:
            new_r, new_c = r + dr, c + dc

            if 0 <= new_r < 3 and 0 <= new_c < 3:   
                new_state = [list(row) for row in state]
                new_state[r][c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[r][c]
                new_state = tuple(tuple(row) for row in new_state)
                if new_state not in self.visited:
                    self.visited.add(new_state)
                    successors.append((action, new_state, 1))
        return successors
    

problem = Puzzle(((1, 2, 3), (4, 5, 6), (7, 0, 8)))

bfs_search = BestFirstSearch(problem, lambda state, cost: 0)
#print(bfs_search.search())

dfs_search = BestFirstSearch(problem, lambda state, cost: -cost)
#print(dfs_search.search())

ucs_search = BestFirstSearch(problem, lambda state, cost: cost)
#print(ucs_search.search())

ids_search = IterativeDeepeningSearch(problem)
#print(ids_search.search())