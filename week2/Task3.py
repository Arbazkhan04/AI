from Task1 import Graph


def bfs(graph, start_vertex):
    queue = [start_vertex]
    visited = set()
    path = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            path.append(node)
            visited.add(node)
            for neighbor in graph.adj[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return tuple(path)


def bfs_distance(graph, start_vertex, end_vertex):
    q = [[start_vertex, 0]]
    while q:
        node, level = q.pop(0)
        if node == end_vertex:
            return level
        for nei in graph.adj[node]:
            q.append([nei, level+1])
    return -1


def bfs_number_of_levels(graph, start_vertex, end_vertex):
    q = [[start_vertex, 0]]
    while q:
        node, level = q.pop(0)
        if node == end_vertex:
            return level
        for nei in graph.adj[node]:
            q.append([nei, level+1])
    return -1


def bfs_draw_tree(graph, start_vertex):
    pass

