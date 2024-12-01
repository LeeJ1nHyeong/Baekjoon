'''
호수 개수와 각 호수 별 넓이를 오름차순으로 출력하기

4방향(좌우상하)으로 인접한 영역을 같은 영역으로 취급
'''

from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

lakes = []

for i in range(n):
    for j in range(m):
        if board[i][j] == "0" or visited[i][j]:
            continue

        queue = deque([(i, j)])
        visited[i][j] = 1
        cnt = 1

        while queue:
            ci, cj = queue.popleft()

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == n or nj < 0 or nj == m:
                    continue

                if board[ni][nj] == "0":
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                cnt += 1
                queue.append((ni, nj))

        lakes.append(cnt)

lakes.sort()
print(len(lakes))
print(*lakes)
