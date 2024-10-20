from Problems import GridWorldProblem
from BestFirstSearch import BestFirstSearch, IterativeDeepeningSearch


class MazeSolver(GridWorldProblem):
    def __init__(self, grid, start_state, end_state):
        super().__init__(grid)
        self.start = start_state
        self.end = end_state

    def start_state(self):
        return self.start
    
    def is_end(self, state):
        return state == self.end
    



if __name__ == "__main__":

    grid = [[1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1], 
            [1, 1, 1, 0, 0], 
            [0, 0, 1, 1, 1]]
    maze = MazeSolver(grid, (0, 0), (3, 3))

    bfs_search = BestFirstSearch(maze, lambda state, cost: 0)
    print(bfs_search.search())

    ucs_search = BestFirstSearch(maze, lambda state, cost: cost)
    #print(ucs_search.search())


    # dfs on transportation problem
    dfs_search = BestFirstSearch(maze, lambda state, cost: -cost)
    #print(dfs_search.search())

    ids_search = IterativeDeepeningSearch(maze)
    #print(ids_search.search())