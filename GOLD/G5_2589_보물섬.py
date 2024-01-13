from collections import deque

r, c = map(int, input().split())
treasure = [list(input()) for _ in range(r)]

ans = 0  # L과 L사이 지날 수 있는 최댓값

for i in range(r):
    for j in range(c):
        if treasure[i][j] == "L":
            queue = deque([(i, j, 0)])
            visited = [[0 for _ in range(c)] for _ in range(r)]  # 방문 여부를 확인 하기 위한 2차원 배열
            visited[i][j] = 1  # 방문 표시

            while queue:
                now_i, now_j, cnt = queue.popleft()  # 현재 i, j 좌표, 이동 횟수 cnt
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):  # 현재 위치에서 4방향 탐색
                    ni, nj = now_i + di, now_j + dj
                    # 조건에 부합하면 방문 표시 후 해당 좌표와 이동 횟수를 tuple 형태로 큐에 추가
                    if 0 <= ni < r and 0 <= nj < c and treasure[ni][nj] == "L" and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        queue.append((ni, nj, cnt + 1))
                        ans = max(ans, cnt + 1)

print(ans)