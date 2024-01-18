from collections import deque

def rain(h):
    global max_height

    visited = [[0] * n for _ in range(n)]  # 방문 표시를 위한 리스트
    area = 0  # 안전 영역 개수

    for i in range(n):
        for j in range(n):
            if height[i][j] > h and not visited[i][j]:  # 해당 위치가 잠긴 높이보다 높고 미방문이라면 bfs 시작
                # bfs
                queue = deque([(i, j)])
                visited[i][j] = 1

                while queue:
                    now_i, now_j = queue.popleft()
                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        ni, nj = now_i + di, now_j + dj
                        if 0 <= ni < n and 0 <= nj < n and height[ni][nj] > h and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))

                area += 1  # while문이 끝났다면 안전 영역 1 추가

    return area  # 해당 높이 이상에서의 안전 영역 값 return

n = int(input())
height = [list(map(int, input().split())) for _ in range(n)]

max_height = 1  # 최대높이
max_area = 0  # 최대 안전 영역 개수

# 최대 높이 구하기
for i in range(n):
    for j in range(n):
        max_height = max(max_height, height[i][j])

# 최대 안전영역 개수
for h in range(max_height):  # 모든 지역이 안 잠기는 경우도 있기 때문에 0부터 시작
    max_area = max(max_area, rain(h))

print(max_area)