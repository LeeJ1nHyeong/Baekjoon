''' 문제 설명

0과 1로 이루어진 그리드
Operation M : x, y 좌표의 숫자를 z로 변경
Operation Q : 그리드 내에 있는 1로 이루어진 영역의 개수 출력

'''

from collections import deque

t = int(input())

for tc in range(1, t + 1):
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]
    n = int(input())

    print(f"Case #{tc}:")
    for _ in range(n):
        operation, *lst = map(str, input().split())

        # Operation Q
        if operation == "Q":
            visited = [[0] * c for _ in range(r)]  # 방문 여부
            cnt = 0  # 영역 개수

            for i in range(r):
                for j in range(c):
                    # 0이거나 방문 지역은 탐색 제외
                    if board[i][j] == "0":
                        continue
                    if visited[i][j]:
                        continue

                    # bfs 초기 세팅
                    queue = deque([(i, j)])
                    visited[i][j] = 1

                    # bfs 진행
                    while queue:
                        ci, cj = queue.popleft()

                        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                            ni, nj = ci + di, cj + dj

                            if ni < 0 or ni == r or nj < 0 or nj == c:
                                continue

                            if board[ni][nj] == "0":
                                continue

                            if visited[ni][nj]:
                                continue

                            # 조건을 만족하는 위치에 대해 방문 표시 후 queue에 추가
                            visited[ni][nj] = 1
                            queue.append((ni, nj))

                    # bfs 종료 후 cnt 1 추가
                    cnt += 1

            # 영역 개수 출력
            print(cnt)

        # Operation M
        elif operation == "M":
            # 숫자를 교체 진행
            i, j, change = lst
            board[int(i)][int(j)] = change
