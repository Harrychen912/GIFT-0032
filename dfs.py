# writing your code here

from node import Node

def dfs(start, end):
    stack = [start]
    visited = set()
    came_from = {}
    visit_history = []

    while stack:
        current = stack.pop()
        visit_history.append(current)
        if current == end:
            return reconstruct_path(came_from, current), visit_history

        visited.add(current)

        for neighbor in current.get_neighbors():
            if neighbor not in visited  and neighbor not in stack and neighbor.type != 'wall':
                stack.append(neighbor)
                came_from[neighbor] = current

    return None  # No path found

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path