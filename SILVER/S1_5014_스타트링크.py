def bfs(f, s, g, u, d):  # BFS
    queue = deque([s])
    visited = [-1] * (f + 1)  # 층 방문 여부를 확인하기 위한 리슽

    visited[s] = 0  # 첫 층 방문 표시

    while queue:
        floor = queue.popleft()
        if floor == g:
            return visited[floor]  # 원하는 층에 도달하면 해당 층의 visited 인덱스 출력
        
        # 위, 아래 이동 후 해당 층을 방문하지 않았을 경우 visited의 이동 후 인덱스에 1 추가 후 queue에 추가
        if 0 < floor + u <= f and visited[floor + u] == -1:
            visited[floor + u] = visited[floor] + 1
            queue.append(floor + u)
        if 0 < floor - d <= f and visited[floor - d] == -1:
            visited[floor - d] = visited[floor] + 1
            queue.append(floor - d)

    return "use the stairs"  # queue가 비었으면 이동하지 못하므로 문구 출력

from collections import deque

f, s, g, u, d = map(int, input().split())

print(bfs(f, s, g, u, d))