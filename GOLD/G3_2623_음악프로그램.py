import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
route = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
result = []
queue = deque()

for _ in range(M):
    num_singer, *singers = map(int, input().split())
    for i in range(num_singer - 1):
        route[singers[i]].append(singers[i + 1])
        inDegree[singers[i + 1]] += 1

for i in range(1, N + 1):
    if not inDegree[i]:
        queue.append(i)

while queue:
    now = queue.popleft()
    result.append(now)
    for node in route[now]:
        inDegree[node] -= 1
        if not inDegree[node]:
            queue.append(node)

if len(result) != N:
    print(0)
else:
    for r in result:
        print(r)