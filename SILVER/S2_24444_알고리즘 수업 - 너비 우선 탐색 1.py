from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 각 노드 별로 연결되어있는 다음 노드들을 오름차순으로 정렬
for t in tree:
    t.sort()

queue = deque()
queue.append(r)
visited[r] = 1

turn = 1
while queue:
    now = queue.popleft()

    for node in tree[now]:
        if visited[node]:
            continue

        turn += 1
        visited[node] = turn
        queue.append(node)

for i in range(1, n + 1):
    print(visited[i])
