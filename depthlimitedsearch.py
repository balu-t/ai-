def dls(node, goal, depth):

    if node == goal:
        return True

    if depth <= 0:
        return False

    for child in graph[node]:
        if dls(child, goal, depth-1):
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

print("Depth Limited Search:", dls('A','F',2))