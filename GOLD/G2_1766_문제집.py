import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
route = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
result = []
queue = []

for _ in range(M):
    a, b = map(int, input().split())
    route[a].append(b)
    inDegree[b] += 1

for i in range(1, N + 1):
    if not inDegree[i]:
        heapq.heappush(queue, i)

while queue:
    now = heapq.heappop(queue)
    result.append(now)
    for node in route[now]:
        inDegree[node] -= 1
        if not inDegree[node]:
            heapq.heappush(queue, node)

print(*result)