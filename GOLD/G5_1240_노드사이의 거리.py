from collections import deque


def bfs(start, end):
    # bfs 초기 세팅
    visited = [0] * (n + 1)  # 방문 여부 체크용 리스트
    visited[start] = 1
    queue = deque([(start, 0)])

    # bfs 진행
    while queue:
        now, dist = queue.popleft()

        # 현재 노드와 연결되어 있는 미방문 노드 탐색
        for node in nodes[now]:
            # 다음 노드가 도착점이라면 거리를 더해준 값을 return
            if node[0] == end:
                return dist + node[1]
            
            # 미방문 노드를 방문 처리 후 거리를 더해준 값과 같이 queue에 추가
            if not visited[node[0]]:
                visited[node[0]] = 1
                queue.append((node[0], dist + node[1]))


n, m = map(int, input().split())
nodes = [[] for _ in range(n + 1)]  # 노드 간의 간선 정보를 담을 2차원 리스트

# 노드 간의 거리를 양방향으로 저장
for _ in range(n - 1):
    s, e, d = map(int, input().split())
    nodes[s].append((e, d))
    nodes[e].append((s, d))

for _ in range(m):
    i, j = map(int, input().split())
    print(bfs(i, j))  # bfs 진행
    