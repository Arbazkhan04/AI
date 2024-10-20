import heapq

class BidirectionalBestFirstSearch:
    def __init__(self, problem, priority_function):
        self.problem = problem
        self.priority_function = priority_function

    def search(self):
        start = self.problem.start_state()
        goal = self.problem.goal_state()

        if start == goal:
            return [start]

        # Forward search from start
        forward_frontier = []
        heapq.heappush(forward_frontier, (self.priority_function(start, 0), start))
        forward_explored = set()
        forward_parent = {start: None}
        forward_cost_so_far = {start: 0}

        # Backward search from goal
        backward_frontier = []
        heapq.heappush(backward_frontier, (self.priority_function(goal, 0), goal))
        backward_explored = set()
        backward_parent = {goal: None}
        backward_cost_so_far = {goal: 0}

        # Intersection point for path reconstruction
        meeting_point = None

        while forward_frontier and backward_frontier:
            # Forward search step
            forward_meeting = self.search_step(forward_frontier, forward_explored, forward_parent, forward_cost_so_far, backward_explored, direction="forward")
            if forward_meeting:
                meeting_point = forward_meeting
                break

            # Backward search step
            backward_meeting = self.search_step(backward_frontier, backward_explored, backward_parent, backward_cost_so_far, forward_explored, direction="backward")
            if backward_meeting:
                meeting_point = backward_meeting
                break

        if meeting_point is not None:
            return self.reconstruct_path(forward_parent, backward_parent, meeting_point), forward_cost_so_far[meeting_point] + backward_cost_so_far[meeting_point]
        
        return None

    def search_step(self, frontier, explored, parent, cost_so_far, other_explored, direction):
        priority, state = heapq.heappop(frontier)

        if state in other_explored:
            return state  # Found a meeting point

        explored.add(state)

        for action, next_state, cost in self.problem.successors(state):
            new_cost = cost_so_far[state] + cost
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = self.priority_function(next_state, new_cost)
                heapq.heappush(frontier, (priority, next_state))
                parent[next_state] = state

        return None

    def reconstruct_path(self, forward_parent, backward_parent, meeting_point):
        # Reconstruct the path from start to the meeting point in the forward search
        path_from_start = []
        state = meeting_point
        while state is not None:
            path_from_start.append(state)
            state = forward_parent[state]
        path_from_start = list(reversed(path_from_start))

        # Reconstruct the path from the meeting point to the goal in the backward search
        path_to_goal = []
        state = backward_parent[meeting_point]
        while state is not None:
            path_to_goal.append(state)
            state = backward_parent[state]

        # Combine both halves of the path
        return path_from_start + path_to_goal

