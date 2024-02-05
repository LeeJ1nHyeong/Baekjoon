from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  # 이어져있는 0의 영역 구분을 나타내기 위한 2차원 배열
num_cnt = [0]  # 각 영역별 개수를 저장하기 위한 리스트, 인덱스 구분을 위해 0이 들어있는 상태로 시작

# 0의 영역 설정
# board의 0을 찾아 이어져있는 0의 영역을 num으로 표시 후 해당 영역의 넓이를 num_cnt에 저장
num = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == "0" and not visited[i][j]:
            visited[i][j] = num
            queue = deque([(i, j)])
            cnt = 1

            while queue:
                now_i, now_j = queue.popleft()
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    ni, nj = now_i + di, now_j + dj
                    if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == "0" and not visited[ni][nj]:
                        visited[ni][nj] = num
                        cnt += 1
                        queue.append((ni, nj))

            num_cnt.append(cnt)
            num += 1

for i in range(n):
    for j in range(m):
        if board[i][j] == "1":
            num_list = []  # 4방향의 영역 번호를 담기 위한 배열, 중복 방지
            cnt = 1  # 현재 위치도 cnt에 포함하므로 1로 시작
            # 벽(1) 위치에서 4방향 탐색하여 num_list에 없는 값을 index로 하여 num_cnt 값을 cnt에 더해주고 num_list에 추가
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] not in num_list:
                    cnt += num_cnt[visited[ni][nj]]
                    num_list.append(visited[ni][nj])

            board[i][j] = str(cnt % 10)  # 문제 조건에 맞게 10을 나눈 나머지 값을 board에 저장

for b in board:
    print("".join(b))