from collections import deque

def bfs(graph, start, goal):

    visited = []
    queue = deque()

    visited.append(start)
    queue.append(start)

    while queue:

        node = queue.popleft()
        print("Visited:", node)

        if node == goal:
            print("Goal Found!")
            return

        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A', 'F')