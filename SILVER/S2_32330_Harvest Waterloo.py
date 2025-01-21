'''
농장 호박 수확하기
S : small (1$)
M : medium (5$)
L : large (10$)
* : 벽 (통과 불가)

시작 지점 (a, b)에서 수확할 수 있는 호박의 총 가격 구하기

'''

from collections import deque

r = int(input())
c = int(input())
farm = [list(input()) for _ in range(r)]
a = int(input())
b = int(input())

visited = [[0] * c for _ in range(r)]
small, medium, large = 0, 0, 0

queue = deque([(a, b)])
visited[a][b] = 1

while queue:
    ci, cj = queue.popleft()

    if farm[ci][cj] == "S":
        small += 1
    elif farm[ci][cj] == "M":
        medium += 1
    elif farm[ci][cj] == "L":
        large += 1

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj

        if ni < 0 or ni == r or nj < 0 or nj == c:
            continue

        if farm[ni][nj] == "*":
            continue

        if visited[ni][nj]:
            continue

        visited[ni][nj] = 1
        queue.append((ni, nj))

ans = small + medium * 5 + large * 10
print(ans)
