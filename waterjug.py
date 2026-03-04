from collections import deque

def water_jug_bfs(jug1, jug2, target):

    visited = set()
    queue = deque([(0,0)])

    while queue:

        x, y = queue.popleft()

        if (x,y) in visited:
            continue

        print(x,y)

        visited.add((x,y))

        if x == target or y == target:
            print("Target Reached")
            return

        queue.append((jug1,y))
        queue.append((x,jug2))
        queue.append((0,y))
        queue.append((x,0))

        transfer = min(x, jug2-y)
        queue.append((x-transfer, y+transfer))

        transfer = min(y, jug1-x)
        queue.append((x+transfer, y-transfer))


water_jug_bfs(4,3,2)