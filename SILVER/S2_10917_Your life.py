from collections import deque


def bfs():
    # bfs 초기 세팅
    queue = deque([(1, 0)])
    visited[1] = 1

    # bfs 진행
    while queue:
        now, move = queue.popleft()

        # n번 상황에 도달했다면 이동 횟수 return
        if now == n:
            return move
        
        # 현재의 상황과 연결된 다른 상황들 중 미방문 지역이 있다면 방문 표시 후 queue에 추가
        for dream in dreams[now]:
            if not visited[dream]:
                visited[dream] = 1
                queue.append((dream, move + 1))

    return -1  # while문이 종료됐다면 이동 불가라는 뜻이므로 -1 return


n, m = map(int, input().split())
dreams = [[] for _ in range(n + 1)]  # 노드 간의 간선 저장용 2차원 리스트
visited = [0] * (n + 1)

# 노드간의 간선을 단방향으로 저장
for _ in range(m):
    x, y = map(int, input().split())
    dreams[x].append(y)

print(bfs())