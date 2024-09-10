from collections import deque


def bfs():
    # bfs 초기 세팅
    queue = deque([(n, 0)])
    visited[n] = 1

    # bfs 진행
    while queue:
        now, move = queue.popleft()

        if now == m:
            return move
        
        # 좌우 이동
        for d in [-1, 1, -a, a, -b, b]:
            next_stone = now + d

            # 0 ~ 100000 범위 내에서 미방문 지역이라면 해당 지역 방문 표시 후 queue에 추가
            if 0 <= next_stone <= 100000 and not visited[next_stone]:
                visited[next_stone] = 1
                queue.append((next_stone, move + 1))

        # 점프 이동
        for d in [a, b]:
            jump = now * d

            # 0 ~ 100000 범위 내에서 미방문 지역이라면 해당 지역 방문 표시 후 queue에 추가
            if 0 <= jump <= 100000 and not visited[jump]:
                visited[jump] = 1
                queue.append((jump, move + 1))


a, b, n, m = map(int, input().split())
visited = [0] * 100001

print(bfs())
