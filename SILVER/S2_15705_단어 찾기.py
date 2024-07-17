def search():
    for i in range(n):
        for j in range(m):
            # 단어의 첫 문자를 찾으면 탐색 시작
            if board[i][j] == s[0]:
                # 현재 위치 기준 8방향으로 탐색
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
                    ni, nj = i, j
                    idx = 1  # 탐색 문자 인덱스
                    while True:
                        # 원하는 단어를 찾으면 1 return
                        if idx == len(s):
                            return 1
                        
                        # 탐색 방향 1칸 전진
                        ni += di
                        nj += dj

                        # 범위 밖을 벗어나면 break
                        if ni < 0 or ni == n or nj < 0 or nj == m:
                            break

                        # 원하는 문자가 나오지 않는다면 break
                        if board[ni][nj] != s[idx]:
                            break

                        # 원하는 문자를 찾으면 다음 인덱스로 이동
                        idx += 1

    return 0  # 원하는 단어가 없다면 0 return


s = input()
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

print(search())
