from Task1 import Graph


def is_acyclic(graph, start_vertex):
    if graph.is_directed:
        return Dir(graph)
    else:
        return Undir(graph)
    

def Undir(graph):

    def dfs_helper(node, visit, parent):
        visit.add(node)
        for nei in graph.adj[node]:
            if nei not in visit:
                if dfs_helper(nei, visit, node):
                    return True
            elif nei != parent:
                return True
        return False
    

    visit = set()
    for node in graph.adj.keys():
        if node not in visit:
            if dfs_helper(node, visit, None):
                return False    
    return True



def Dir(graph):
    degrees = {node: 0 for node in graph.adj}

    for source, dest in graph.edges:
        degrees[dest] += 1
    
    q = [node for node in graph.adj if degrees[node] == 0]
    visited = 0

    while q:
        node = q.pop(0)
        visited += 1

        for nei in graph.adj[node]:
            degrees[nei] -= 1
            if degrees[nei] == 0:
                q.append(nei)
    return visited == len(graph.adj)