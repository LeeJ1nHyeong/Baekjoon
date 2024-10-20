from collections import deque

n = int(input())
bridge = list(map(int, input().split()))
visited = [0] * n

s = int(input())
s -= 1

# bfs 초기 세팅
queue = deque([s])
visited[s] = 1

# bfs 진행
while queue:
    now = queue.popleft()

    d = bridge[now]

    # 현재 위치에서 점프로 이동할 수 있는 위치 탐색
    for di in [-d, d]:
        ni = now + di

        if ni < 0 or ni >= n:
            continue

        if visited[ni]:
            continue

        # 조건을 만족하는 미방문 지역에 대해 방문 표시 후 queue에 추가
        visited[ni] = 1
        queue.append(ni)

# 방문 가능한 돌의 개수 출력
print(sum(visited))
