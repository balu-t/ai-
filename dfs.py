def dfs(graph, start, goal):

    visited = []
    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:

            print("Visited:", node)
            visited.append(node)

            if node == goal:
                print("Goal Found!")
                return

            for neighbor in graph[node]:
                stack.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A', 'F')