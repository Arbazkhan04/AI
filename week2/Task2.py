from Task1 import Graph

def dfs(graph, start_vertex):
    path = []
    visit = set()

    def dfs_recur(node, visited):
        visited.add(node)
        path.append(node)
        for neighbor in graph.adj[node]:
            if neighbor not in visited:
                dfs_recur(neighbor, visited)
    
    dfs_recur(start_vertex, visit)
    return tuple(path)

    # draw dfs
def dfs_draw_tree(graph, start_vertex):
    pass

