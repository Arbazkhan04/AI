from Graph import Graph
from BestFirstSearch import BestFirstSearch, IterativeDeepeningSearch



class MissionariesAndCannibals:
    def __init__(self):
        self.graph = Graph()
        self._build_graph()

    def _build_graph(self):
        visited = set()
        frontier = [self.start_state()]

        actions = [[1, 0], [0, 1], [1, 1], [2, 0], [0, 2]]

        while frontier:
            state = frontier.pop()
            if state in visited:
                continue

            visited.add(state)
            self.graph.add_node(state=state)

            m_left, c_left, boat = state

            for m, c in actions:

                if boat:    # boat at the right bank of the river
                    newState = (m_left + m, c_left + c, 0)
                else:       # at the left bank
                    newState = (m_left - m, c_left - c, 1)
                
                if self.validState(newState):
                    self.graph.add_edge(state, f"{m}M and {c}C", 1, newState)
                    if newState not in visited:
                        frontier.append(newState)
            

    def start_state(self):
        return (3, 3, 0)

    def is_end(self, state):
        return state == (0, 0, 1)


    def validState(self, state):
        m_left, c_left, boat = state
        m_right, c_right = 3 - m_left, 3 - c_left
        return (0 <= m_left <= 3) and (0 <= c_left <= 3) and (0 <= m_right <= 3) and (0 <= c_right <= 3) and (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right)
    
    
    def successors(self, state):
        node = self.graph.get_node(state=state)
        return [(edge.action, edge.next_node.state, edge.cost) for edge in node.edges]


# storing states such that at any state is tells us the number of 
# m and c on the left bank and the third one tells us location of boat

problem = MissionariesAndCannibals()

bfs_search = BestFirstSearch(problem, lambda state, cost: 0)
#print(bfs_search.search())

dfs_search = BestFirstSearch(problem, lambda state, cost: -cost)
#print(dfs_search.search())

ucs_search = BestFirstSearch(problem, lambda state, cost: cost)
#print(ucs_search.search())

ids_search = IterativeDeepeningSearch(problem)
#print(ids_search.search())
