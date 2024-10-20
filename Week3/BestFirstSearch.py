import heapq

class BestFirstSearch:
    def __init__(self, problem, priority_function):
        self.problem = problem
        self.priority_function = priority_function

    def search(self):
        start = self.problem.start_state()
        if self.problem.is_end(start):
            return [start]
        
        frontier = []
        heapq.heappush(frontier, (self.priority_function(start, 0), start))
        explored = set()
        parent = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            priority, state = heapq.heappop(frontier)

            if self.problem.is_end(state):
                path = []
                current = state
                while state is not None:
                    path.append(state)
                    state = parent[state]
                return list(reversed(path)), cost_so_far[current]
            
            for action, next_state, cost in self.problem.successors(state):
                new_cost = cost_so_far[state] + cost
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    priority = self.priority_function(next_state, new_cost)
                    heapq.heappush(frontier, (priority, next_state))
                    parent[next_state] = state
            
        return None
    

class IterativeDeepeningSearch:
    def __init__(self, problem):
        self.problem = problem
    
    def search(self):
        depthLimit = 0
        while True:
            result = self.depthLimitedSearch(depthLimit)
            if result is not None:
                return result
            depthLimit += 1
    
    def depthLimitedSearch(self, depthLimit):

        def ids_priority(state, depth):
            return -depth if depth <= depthLimit else float('inf')
        
        search = BestFirstSearch(self.problem, ids_priority)
        return search.search()