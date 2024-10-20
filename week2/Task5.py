from Task1 import Graph
import heapq

def distance_dijxtra(graph, start_vertex,end_vertex):
    heap = [(0, start_vertex)]
    visit = set()
    prev = {}
    distance = {start_vertex: 0}

    while heap:
        dist, node = heapq.heappop(heap)
        if node in visit:
            continue
        visit.add(node)

        if node == end_vertex:
            path = []
            while node in prev:
                path.append(node)
                node = prev[node]
            path.append(start_vertex)
            return (dist, path.reverse())
        
        for nei, d in graph.adj[node]:
            if nei not in visit:
                if dist + d < distance.get(nei, float('inf')):
                    distance[nei] = dist + d
                    prev[nei] = node
                    heapq.heappush(heap, (dist + d, nei))
    return -1

def distance_bellmanford (graph, start_vertex,end_vertex):
    pass
