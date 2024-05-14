from collections import deque
import sys
input = sys.stdin.readline


def check():
    # 검사 위치에 곰팡이가 있으면 "YES" return
    for check_i, check_j in check_list:
        if visited[check_i - 1][check_j - 1][t % 2]:
            return "YES"

    return "NO"  # 곰팡이가 없다면 "NO" return


n, m, k, t = map(int, input().split())

# 짝수일과 홀수일의 곰팡이 존재 여부를 확인하기 위한 3차원 리스트
visited = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]

# 초기의 곰팡이 위치를 queue에 추가하면서 짝수일(0)에 방문 표시
queue = deque([])
for _ in range(m):
    i, j = map(int, input().split())
    visited[i - 1][j - 1][0] = 1
    queue.append((i - 1, j - 1, 0))

# bfs 진행
while queue:
    i, j, day = queue.popleft()

    # 검사일(t)일 경우 continue
    if day == t:
        continue

    next_area = 0  # 현재 위치에서 다음 위치로 퍼지는 횟수
    for di, dj in (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2):
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= n:
            continue
        # 짝수일은 홀수일, 홀수일은 짝수일의 방문 여부를 확인하여 방문이 되어있을 경우 continue
        if visited[ni][nj][(day + 1) % 2]:
            continue
        # 방문이 되어있지 않다면 방문 표시 후 queue에 추가
        visited[ni][nj][(day + 1) % 2] = 1
        queue.append((ni, nj, day + 1))
        next_area += 1  # queue 추가 후 next_area 1 추가

    # 현재 위치에서 다음 위치로 퍼지지 않는다면 현재 위치를 미방문 표시
    if not next_area:
        visited[i][j][day % 2] = 0

# 검사 위치
check_list = []
for _ in range(k):
    check_list.append(tuple(map(int, input().split())))

print(check())  # 방 검사 진행
