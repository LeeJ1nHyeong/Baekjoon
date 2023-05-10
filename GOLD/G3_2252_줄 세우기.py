import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
route = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
result = []
queue = deque()

for _ in range(M):
    students = list(map(int, input().split()))
    for i in range(len(students) - 1):
        route[students[i]].append(students[i + 1])
        inDegree[students[i + 1]] += 1

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

print(*result)