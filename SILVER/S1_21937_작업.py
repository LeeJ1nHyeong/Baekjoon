from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nodes = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# b -> a 단방향 간선을 저장
for _ in range(m):
    a, b = map(int, input().split())
    nodes[b].append(a)

x = int(input())  # 끝내야 할 작업

cnt = 0

# x번 작업을 시작점으로 하여 bfs 탐색 진행
queue = deque([x])
visited[x] = 1

while queue:
    now = queue.popleft()

    # 미방문 지역에 대해 방문 표시 후 cnt 1 추가 및 queue에 추가
    for node in nodes[now]:
        if not visited[node]:
            visited[node] = 1
            cnt += 1
            queue.append(node)

# x번 작업 진행 전 해야할 작업 개수 출력
print(cnt)
