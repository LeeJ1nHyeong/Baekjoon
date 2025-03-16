from collections import deque

n, k = map(int, input().split())
network = [[] for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

small_network = True
for i in range(1, n + 1):
    visited = [0] * (n + 1)
    visited[i] = 1
    queue = deque([(i, 0)])

    while queue:
        now, cnt = queue.popleft()

        if cnt > 6:
            small_network = False
            break

        for node in network[now]:
            if not visited[node]:
                visited[node] = 1
                queue.append((node, cnt + 1))

    if sum(visited) != n:
        small_network = False

    if not small_network:
        break

print("Small World!" if small_network else "Big World!")
