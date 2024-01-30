from collections import deque

def bfs():  # bfs
    queue = deque([(0, 0, 0, 0)])  # (i, j, 이동 횟수, 그람 보유 여부)

    while queue:
        i, j, move, gram = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and move < t:
                if ni == n - 1 and nj == m - 1:  # 공주 좌표에 도달하면 move + 1을 return
                    return move + 1
                
                # 그람 보유 여부에 따라 조건 분기
                # 그람 미보유
                if not gram:
                    if castle[ni][nj] == 0 and not visited[ni][nj][0]:
                        visited[ni][nj][0] = 1  # 그람 미보유했을 때의 방문 표시
                        queue.append((ni, nj, move + 1, 0))
                    elif castle[ni][nj] == 2:  # 다음 지역이 그람이라면 gram을 1로 넣고 큐에 추가
                        visited[ni][nj][0] = 1
                        queue.append((ni, nj, move + 1, 1))

                # 그람 보유
                else:
                    if not visited[ni][nj][1]:  # 그람 보유했을 때의 방문 표시
                        visited[ni][nj][1] = 1
                        queue.append((ni, nj, move + 1, gram))

    return "Fail"  # while문이 종료됐다면 구출 실패이므로 "Fail" return

n, m, t = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]  # 그람 보유 여부에 따른 방문 표시 3차원 배열
visited[0][0][0] = 1  # 처음 좌표(그람 미보유) 방문 표시

print(bfs())