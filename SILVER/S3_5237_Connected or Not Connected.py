'''
그래프 내 모든 노드가 연결되어 있다면 "Connected."
연결되지 않은 노드가 있다면 "Not connected."
'''

from collections import deque

t = int(input())

for _ in range(t):
    n, k, *pair = map(int, input().split())
    tree = [[] for _ in range(n)]
    visited = [0] * n

    for i in range(k):
        s, e = pair[2 * i], pair[2 * i + 1]
        tree[s].append(e)
        tree[e].append(s)

    queue = deque([0])
    visited[0] = 1

    while queue:
        now = queue.popleft()

        for node in tree[now]:
            if not visited[node]:
                visited[node] = 1
                queue.append(node)

    print("Not connected." if 0 in visited else "Connected.")
