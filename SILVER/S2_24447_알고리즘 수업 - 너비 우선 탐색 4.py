from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)  # 방문 순서
depth = [0] * (n + 1)  # 각 노드의 깊이

for _ in range(m):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 각 노드와 연결된 다음 노드를 오름차순으로 정렬
for t in tree:
    t.sort()

queue = deque()
queue.append((r, 0))
visited[r] = 1
depth[r] = 0

turn = 1
while queue:
    now, d = queue.popleft()

    for node in tree[now]:
        if visited[node]:
            continue

        turn += 1
        visited[node] = turn
        depth[node] = d + 1
        queue.append((node, d + 1))

ans = 0
for i in range(1, n + 1):
    ans += visited[i] * depth[i]

print(ans)
