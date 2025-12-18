from collections import deque

def bfs(g, start):
    q = deque([start])
    seen = {start}
    while q:
        v = q.popleft()
        for nv in g.get(v, []):
            if nv not in seen:
                seen.add(nv)
                q.append(nv)
    return seen
