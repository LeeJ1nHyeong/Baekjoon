n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

ans = n * m  # 다시 색칠해야하는 체스판 칸의 최솟값

# 8X8 체스판의 좌상단 좌표 기준으로 인덱스 설정
for r in range(n - 7):
    for c in range(m - 7):
        # BW, WB 두 패턴 형태의 경우로 생각
        bw, wb = 0, 0
        for i in range(r, r + 8):
            for j in range(c, c + 8):
                # 두 인덱스 합이 홀수인 경우와 짝수인 경우로 나누기
                if (i + j) % 2:
                    if board[i][j] != "B":
                        wb += 1
                    else:
                        bw += 1

                else:
                    if board[i][j] != "W":
                        wb += 1
                    else:
                        bw += 1

        # 최솟값을 ans에 저장
        ans = min(ans, bw, wb)

print(ans)
