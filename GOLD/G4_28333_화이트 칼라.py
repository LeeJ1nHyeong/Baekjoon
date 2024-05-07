'''
1. bfs로 1번부터 n번까지 탐색하면서 최단 거리일 경우 이전 방문 도시를 저장하면서 탐색
2. n번부터 이전 방문 도시를 저장한 리스트를 역추적하여 도시들을 탐색
'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs():  # 도시 탐색
    visited = [-1] * (n + 1)
    visited[1] = 0

    prev_city = [[] for _ in range(n + 1)]  # 직전 도시를 저장할 2차원 리스트
    queue = deque([1])

    # bfs 진행
    while queue:
        now = queue.popleft()

        for c in city[now]:
            # 미방문 도시이거나 방문 길이가 짧은 도시의 경우 직전 방문 도시 저장 후 queue에 추가
            if visited[c] == -1 or visited[c] > visited[now] + 1:
                visited[c] = visited[now] + 1
                prev_city[c].append(now)
                queue.append(c)
            # 방문 길이가 같은 도시의 경우 직전 방문 도시 저장만 진행
            elif visited[c] == visited[now] + 1:
                prev_city[c].append(now)

    return prev_city  # 직전 방문 도시 리스트 return


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    city = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        city[a].append(b)

    prev_city = bfs()

    # n번 부터 방문 도시를 역추적
    ans = [n]  # 역추적하여 방문한 도시 리스트

    trace_queue = deque([n])  # 역추적 queue
    trace_visited = [0] * (n + 1)  # 역추적 방문 여부 체크용 리스트

    while trace_queue:
        now = trace_queue.popleft()

        for c in prev_city[now]:
            if not trace_visited[c]:
                trace_visited[c] = 1
                ans.append(c)
                trace_queue.append(c)

    # 역추적하여 추가한 도시 리스트 오름차순 후 출력
    ans.sort()
    print(*ans)
