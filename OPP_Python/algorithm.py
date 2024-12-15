import heapq
from flask import g

def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {start: 0}
    previous_nodes = {start: None}
    
    while queue:
        (dist, node) = heapq.heappop(queue)
        
        if node == end:
            path = []
            while previous_nodes[node] is not None:
                path.insert(0, node)
                node = previous_nodes[node]
            path.insert(0, start)
            return path
        
        for neighbor, weight in graph.get(node, {}).items():
            distance = dist + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                previous_nodes[neighbor] = node
    return None

def a_star(graph, start, end, heuristic):
    open_list = [(0, start)]
    g_scores = {start: 0}
    f_scores = {start: heuristic(start, end)}
    previous_nodes = {start: None}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == end:
            path = []
            while previous_nodes[current] is not None:
                path.insert(0, current)
                current = previous_nodes[current]
            path.insert(0, start)
            return path
        
        for neighbor, weight in graph.get(current, {}).items():
            tentative_g_score = g
