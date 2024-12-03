'''
밭에 씨를 뿌리는 영역 중 가장 넓은 영역의 넓이 출력

8방향 인접한 부분에 있는 풀(".")은 같은 영역으로 취급
'''

from collections import deque

w, h = map(int, input().split())
board = [list(input()) for _ in range(h)]
visited = [[0] * w for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if board[i][j] == "*" or visited[i][j]:
            continue

        queue = deque([(i, j)])
        visited[i][j] = 1
        cnt = 1

        while queue:
            ci, cj = queue.popleft()

            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                ni, nj = ci + di, cj + dj

                if ni < 0 or ni == h or nj < 0 or nj == w:
                    continue

                if board[ni][nj] == "*":
                    continue

                if visited[ni][nj]:
                    continue

                visited[ni][nj] = 1
                cnt += 1
                queue.append((ni, nj))

        ans = max(ans, cnt)

print(ans)
