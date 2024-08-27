from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [0] * (n + 1)
    queue = deque([(s, 0)])
    visited[s] = 1

    while queue:
        now, move = queue.popleft()

        # 목표지점에 도착했다면 이동횟수 return
        if now == e:
            return move
        
        # 1칸 이전의 값이 미방문 지역이라면 해당 값을 queue에 추가
        if now - 1 >= 1 and not visited[now - 1]:
            visited[now - 1] = 1
            queue.append((now - 1, move + 1))

        # 1칸 이후의 값이 미방문 지역이라면 해당 값을 queue에 추가
        if now + 1 <= n and not visited[now + 1]:
            visited[now + 1] = 1
            queue.append((now + 1, move + 1))

        # 현재 위치에서 텔레포트로 이동 가능한 곳이 미방문 지역이라면 queue에 추가
        for node in nodes[now]:
            if not visited[node]:
                visited[node] = 1
                queue.append((node, move + 1))


n, m = map(int, input().split())
s, e = map(int, input().split())

nodes = [[] for _ in range(n + 1)]  # 텔레포트 가능 지역을 구현할 2차원 리스트

# 텔레포트로 이동 가능한 구간을 양방향으로 저장
for _ in range(m):
    x, y = map(int, input().split())
    nodes[x].append(y)
    nodes[y].append(x)

print(bfs())
