from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 그래프
visited = [0] * (n + 1)  # 방문 여부 체크용
cnt = 0  # 연결 요소 개수

# 노드 간의 간선 표시
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 미방문 지역을 시작으로 탐색
for i in range(1, n + 1):
    if not visited[i]:
        queue = deque([i])
        visited[i] = 1

        while queue:
            now = queue.popleft()
            for node in graph[now]:
                if not visited[node]:
                    visited[node] = 1
                    queue.append(node)

        cnt += 1  # 탐색 종료 후 연결 요소 개수 1 추가

print(cnt)