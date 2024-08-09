from collections import deque


def bfs():
    # bfs 초기 세팅
    visited = [0] * (n + 1)
    queue = deque([(a, 0)])
    visited[a] = 1

    # bfs 진행
    while queue:
        now, cnt = queue.popleft()

        # 목표점에 도착했다면 치환 횟수 return
        if now == b:
            return cnt
        
        # 현재 위치와 연결되어 있는 노드 탐색
        for g in graph[now]:
            # 방문 지역이라면 continue
            if visited[g]:
                continue

            # 방문 지역이 아니라면 방문 표시 후 queue에 추가
            visited[g] = 1
            queue.append((g, cnt + 1))

    return -1  # while문이 종료됐다면 치환 불가라는 뜻이므로 -1 return


a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 두 노드간의 간선을 양방향으로 저장
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

print(bfs())
