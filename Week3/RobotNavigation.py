from MazeSolving import MazeSolver
from BestFirstSearch import BestFirstSearch, IterativeDeepeningSearch


class RobotNavigator(MazeSolver):
    def __init__(self, grid, start_state, end_state):
        super().__init__(grid, start_state, end_state)




grid = [[1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1], 
        [1, 0, 0, 1, 0], 
        [0, 1, 1, 1, 1]]

robot = RobotNavigator(grid, (0, 0), (1, 3))

bfs_search = BestFirstSearch(robot, lambda state, cost: 0)
print(bfs_search.search())

ucs_search = BestFirstSearch(robot, lambda state, cost: cost)
#print(ucs_search.search())

# dfs on transportation problem
dfs_search = BestFirstSearch(robot, lambda state, cost: -cost)
#print(dfs_search.search())

ids_search = IterativeDeepeningSearch(robot)
#print(ids_search.search())
