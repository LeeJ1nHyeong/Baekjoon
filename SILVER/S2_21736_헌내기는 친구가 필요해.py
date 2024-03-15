from collections import deque


def bfs():
    visited = [[0] * m for _ in range(n)]  # 방문 표시용 2차원 리스트
    cnt = 0  # 사람의 수
    queue = deque()

    # 도연이(I)의 좌표를 queue에 추가
    for i in range(n):
        for j in range(m):
            if campus[i][j] == "I":
                visited[i][j] = 1
                queue.append((i, j))
                break

    # bfs 진행
    while queue:
        i, j = queue.popleft()
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            # 다음 이동 좌표가 사람(P)일 경우 cnt 1 추가
            if 0 <= ni < n and 0 <= nj < m and campus[ni][nj] != "X" and not visited[ni][nj]:
                if campus[ni][nj] == "P":
                    cnt += 1
                visited[ni][nj] = 1
                queue.append((ni, nj))

    # 사람이 하나도 없다면 "TT" return
    if not cnt:
        return "TT"

    return cnt  # 사람 수 return


n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]

print(bfs())
