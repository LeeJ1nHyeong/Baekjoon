from collections import deque

# 교통 정체 구간 표시
def traffic(i, j, d):
    # d == 0일 경우 해당 좌표에만 표시 후 return
    if d == 0:
        board[i][j] = 1
        return
    
    '''
    거리가 d 이하인 모든 구역을 표시할 경우 시간초과가 발생
    거리가 d인 구역만 표시를 진행
    '''

    # 현재 좌표 기준 9시 부터 시계방향으로 격자 범위 내에서 거리가 d인 좌표에 교통 체증 표시
    j -= d
    for di, dj in (-1, 1), (1, 1), (1, -1), (-1, -1):
        for _ in range(d):
            i += di
            j += dj

            if 0 <= i < n and 0 <= j < m:
                board[i][j] = 1

# bfs
def bfs():
    # bfs 초기 세팅
    queue = deque([(0, 0, 0)])  # 시작점(0, 0)과 이동 횟수(0)을 튜플 형태로 queue에 저장한 상태로 시작
    board[0][0] = 1  # 시작점(0, 0) 방문 표시

    # bfs 진행
    while queue:
        i, j, move = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = i + di, j + dj
            # 다음 위치가 도착점일 경우 이동 횟수 + 1 return
            if ni == n - 1 and nj == m - 1:
                return move + 1
            
            # 범위 밖을 벗어날 경우 continue
            if ni < 0 or ni == n or nj < 0 or nj == m:
                continue

            # 교통 정체 구간 또는 방문 표시가 되어있을 경우 continue
            if board[ni][nj]:
                continue

            # 방문 표시 후 이동 횟수 1 증가한 상태로 queue에 추가
            board[ni][nj] = 1
            queue.append((ni, nj, move + 1))

    return 0  # while문이 종료됐다면 도착점까지 이동 불가라는 뜻이므로 0 return


n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]

k = int(input())

# k개의 정체 구역 표시 진행
for i in range(k):
    r, c, d = map(int, input().split())
    traffic(r - 1, c - 1, d)  # 정체 구역 표시

ans = bfs()  # bfs 진행

# ans가 0이 아닐 경우 "YES" 출력, 다음 줄 ans 출력
if ans:
    print("YES")
    print(ans)

# ans가 0일 경우 "NO" 출력
else:
    print("NO")
