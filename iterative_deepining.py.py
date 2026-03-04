def dls(node, goal, depth):

    if node == goal:
        return True

    if depth <= 0:
        return False

    for child in graph[node]:
        if dls(child, goal, depth-1):
            return True

    return False


def iddfs(start, goal, max_depth):

    for depth in range(max_depth):

        if dls(start, goal, depth):
            return True

    return False


graph = {
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}

print("Iterative Deepening Result:", iddfs('A','F',5))