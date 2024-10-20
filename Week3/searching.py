from BestFirstSearch import BestFirstSearch,  IterativeDeepeningSearch
from Problems import TransportationProblem



problem = TransportationProblem(N=1000)

# ids on transportation problem
ids_search = IterativeDeepeningSearch(problem)
#print(ids_search.search())


# Example priority functions for BFS
def bfs_priority(state, cost):
    return 0

# Running BFS on the Transportation Problem
bfs_search = BestFirstSearch(problem, bfs_priority)
#print(bfs_search.search())


# running ucs on transportation problem
ucs_search = BestFirstSearch(problem, lambda state, cost: cost)
#print(ucs_search.search())


# dfs on transportation problem
dfs_search = BestFirstSearch(problem, lambda state, cost: -cost)
#print(dfs_search.search())
