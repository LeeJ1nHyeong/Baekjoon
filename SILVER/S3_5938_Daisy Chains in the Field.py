'''
1번 소와 연결되어있지 않은 소의 번호를 오름차순으로 출력
'''

from collections import deque

n, m = map(int, input().split())
cow = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# 양방향 간선 저장
for _ in range(m):
    s, e = map(int, input().split())
    cow[s].append(e)
    cow[e].append(s)

# 1번 소부터 bfs 진행
queue = deque([1])
visited[1] = 1

while queue:
    now = queue.popleft()

    # 연결되어있는 소 중 미방문 번호에 대해 방문 표시 후 queue에 추가
    for c in cow[now]:
        if not visited[c]:
            visited[c] = 1
            queue.append(c)

# 모든 소가 1번 소와 연결되어있다면 0 출력
if sum(visited[1:]) == n:
    print(0)

# 1번 소와 연결되어있지 않은 소의 번호를 출력
else:
    for i in range(1, n + 1):
        if not visited[i]:
            print(i)
