'''
1. 같은 색의 뿌요가 4개 이상 모여있는지 탐색
2-1. 4개 이상 모여있는 뿌요가 없다면 종료
2-2. 4개 이상 모여있는 뿌요가 있다면 뿌요 제거
3. 뿌요 제거 후 위에서 떨어질 뿌요를 탐색하고 해당 뿌요들을 아래로 이동시키기
4. 4개 이상 모인 뿌요가 없을 때 까지 위 과정 반복
'''

from collections import deque


def puyopuyo():  # 뿌요뿌요 게임
    chain_cnt = 0  # 연쇄 횟수

    # 게임 진행
    while True:
        visited = [[0] * 6 for _ in range(12)]  # 방문 표시용
        j_idx = []  # 제거할 뿌요의 j좌표를 담을 리스트
        for i in range(12):
            for j in range(6):
                # 뿌요 탐색 후 bfs 진행
                if board[i][j] != "." and not visited[i][j]:
                    target = board[i][j]  # 뿌요 색깔
                    visited[i][j] = 1
                    chain = [(i, j)]  # 연결되어있는 뿌요들의 좌표
                    queue = deque([(i, j)])

                    # bfs 진행
                    while queue:
                        now_i, now_j = queue.popleft()
                        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                            ni, nj = now_i + di, now_j + dj
                            if 0 <= ni < 12 and 0 <= nj < 6:
                                if board[ni][nj] == target and not visited[ni][nj]:
                                    visited[ni][nj] = 1
                                    chain.append((ni, nj))
                                    queue.append((ni, nj))

                    # 모여있는 뿌요가 4개 이상이면 제거 진행
                    if len(chain) >= 4:
                        j_idx = add_j(chain, j_idx)  # 제거할 뿌요의 j좌표 추가
                        remove(chain)  # 뿌요 제거

        # 제거할 뿌요가 없다면 while문 종료
        if not j_idx:
            break

        # 뿌요 제거 후 위에서 떨어질 뿌요 탐색
        for j in j_idx:
            add_i = 0  # 떨어질 칸 횟수
            for i in range(12):
                if board[i][j] == ".":
                    add_i += 1
                else:
                    board[i - add_i][j] = board[i][j]
                    if add_i:
                        board[i][j] = "."

        chain_cnt += 1  # 위 과정 종료 후 연쇄 횟수 1 증가

    return chain_cnt  # while문 종료 후 연쇄 횟수 return


def add_j(chain, j_idx):  # j 좌표 추가하기
    for i, j in chain:
        if j not in j_idx:
            j_idx.append(j)

    return j_idx


def remove(chain):  # 뿌요 제거
    for i, j in chain:
        board[i][j] = "."


board = [list(input()) for _ in range(12)]
board.reverse()  # 원활한 구현을 위해 배열 뒤집기

print(puyopuyo())