# writing your code here

import heapq
from node import Node

def a_star(start, end):
    open_heap = []
    heapq.heapify(open_heap)
    
    node_id = 0
    initial_g = 0
    initial_f = initial_g + heuristic(start, end)
    heapq.heappush(open_heap, (initial_f, initial_g, node_id, start))
    node_id += 1

    g_score = {start: initial_g}
    came_from = {}
    visit_history = []
    closed_set = set()
    move_cost = 1
    while open_heap:
        current_f, current_g, _, current = heapq.heappop(open_heap)
        
        if current_g > g_score.get(current, float('inf')):
            continue
        
        if current in closed_set:
            continue
        
        closed_set.add(current)
        visit_history.append(current)
        
        if current == end:
            return reconstruct_path(came_from, current), visit_history
        
        for neighbor in current.get_neighbors():
            if neighbor.type == 'wall':
                continue
            
            tentative_g = current_g + move_cost
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, end)
                heapq.heappush(open_heap, (f_score, tentative_g, node_id, neighbor))
                node_id += 1

    return None, visit_history

def heuristic(node, end):
    dx = abs(node.x - end.x)
    dy = abs(node.y - end.y)
    D = 1       
    D2 = 1.414
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse() 
    return path