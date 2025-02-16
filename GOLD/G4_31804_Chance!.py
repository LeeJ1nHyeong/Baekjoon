from collections import deque


def bfs():
    global ans

    queue = deque([(a, 0, 0)])
    
    # chance 사용 여부에 따른 방문 체크용 2차원 리스트 생성
    visited = [[0] * 2 for _ in range(b + 1)]
    visited[a][0] = 1

    while queue:
        now, cnt, chance = queue.popleft()

        # 목표값에 도달하면 마법 사용 횟수 최솟값 여부 확인
        if now == b:
            ans = min(ans, cnt)
            continue

        if now * 2 <= b and not visited[now * 2][chance]:
            visited[now * 2][chance] = 1
            queue.append((now * 2, cnt + 1, chance))

        if now + 1 <= b and not visited[now + 1][chance]:
            visited[now + 1][chance] = 1
            queue.append((now + 1, cnt + 1, chance))

        if not chance and now * 10 <= b and not visited[now * 10][chance]:
            visited[now * 10][1] = 1
            queue.append((now * 10, cnt + 1, 1))


a, b = map(int, input().split())
ans = 1e9

bfs()
print(ans)
