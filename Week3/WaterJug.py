from BestFirstSearch import BestFirstSearch, IterativeDeepeningSearch


class WaterJug:
    def __init__(self):
        self.jug1 = 4
        self.jug2 = 3
        self.goal = 2

    def start_state(self):
        return (0, 0)
    
    def is_end(self, state):
        return state[0] == self.goal or state[1] == self.goal
    
    def successors(self, state):
        jug1, jug2 = state
        successors = [['fill jug1', (self.jug1, jug2), 1],
                      ['fill jug2', (jug1, self.jug2), 1],
                      [ 'pour jug1 to jug2', (jug1 - min(jug1, self.jug2 - jug2), jug2 + min(jug1, self.jug2 - jug2)), 1],
                      [ 'pour jug2 to jug1', (jug1 + min(jug2, self.jug1 - jug1), jug2 - min(jug2, self.jug1 - jug1)), 1], 
                      [ "empty jug1", (0, jug2), 1],
                      [ 'empty jug2', (jug1, 0), 1]]
        return successors
    

problem = WaterJug()
bfs_search = BestFirstSearch(problem, lambda state, cost: 0)
print(bfs_search.search())

ucs_search = BestFirstSearch(problem, lambda state, cost: cost)
print(ucs_search.search())

dfs_search = BestFirstSearch(problem, lambda state, cost: -cost)
print(dfs_search.search())

ids_search = IterativeDeepeningSearch(problem)
print(ids_search.search())

