import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(N)

    while True:
        now = queue.popleft()
        if now == K:
            return visited[now]

        for x in [now - 1, now + 1, now * 2]:
            if 0 <= x <= 100000 and (visited[x] == -1 or visited[x] > visited[now]):
                if x != now * 2:
                    visited[x] = visited[now] + 1
                else:
                    visited[x] = visited[now]
                queue.append(x)

N, K = map(int, input().split())
visited = [-1] * 100001
visited[N] = 0

print(bfs())