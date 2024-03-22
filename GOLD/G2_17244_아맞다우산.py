'''
1. 시작위치(S) 좌표를 찾고, 물건(X)을 찾아 개수를 세면서 각 물건에 번호를 부여하여 저장
2. X의 개수를 바탕으로 방문 표시용 3차원 리스트 생성
3. S부터 bfs를 시작하여 각 물건의 번호를 비트마스킹 형식으로 저장(순서 상관 X) 후 그 값을 활용하여 방문 표시
4. 모든 물건을 다 찾은 상태에서 출구(E)를 찾게 되면 bfs 종료
'''

from collections import deque


def bfs():
    x = 0  # 물건 개수
    si, sj = 0, 0  # 시작 좌표

    queue = deque()

    x_num = 1  # 물건 번호
    for i in range(m):
        for j in range(n):
            # 시작 좌표를 (i, j, 찾은 물건의 비트마스킹 값, 이동 횟수) 형태로 queue에 저장
            if board[i][j] == "S":
                queue.append((i, j, 0, 0))
                si, sj = i, j
            # 물건에 해당 하는 위치에 번호 부여
            elif board[i][j] == "X":
                x += 1
                board[i][j] = str(x_num)
                x_num += 1

    # 물건 개수를 바탕으로 생성한 방문 표시용 3차원 리스트
    # 비트마스킹 값을 활용하므로 2 ** (x + 1) - 1 개로 생성
    visited = [[[0 for _ in range(2 ** (x + 1) - 1)] for _ in range(n)] for _ in range(m)]

    visited[si][sj][0] = 1  # 시작 좌표 방문 표시

    # bfs
    while queue:
        i, j, x_comp, move = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                # 물건을 모두 찾은 상태에서 다음 좌표가 출구라면 bfs 종료
                if board[ni][nj] == "E" and x_comp == 2 ** (x + 1) - 2:
                    return move + 1
                
                # 벽이 아닐 경우
                if board[ni][nj] != "#":
                    # 다음 좌표가 숫자이고 이 숫자가 찾은 물건 명단에 없다면 해당 물건을 비트마스킹 형식으로 저장 후 queue에 추가
                    if board[ni][nj].isdigit() and not (x_comp & (1 << int(board[ni][nj]))):
                        visited[ni][nj][x_comp + 2 ** int(board[ni][nj])] = 1
                        queue.append((ni, nj, x_comp + 2 ** int(board[ni][nj]), move + 1))
                    # 다음 좌표가 벽이 아닌 미방문 좌표라면 방문 표시 후 queue에 추가
                    else:
                        if not visited[ni][nj][x_comp]:
                            visited[ni][nj][x_comp] = 1
                            queue.append((ni, nj, x_comp, move + 1))


n, m = map(int, input().split())
board = [list(input()) for _ in range(m)]

print(bfs())
