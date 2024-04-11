n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = board[0]  # 첫 행을 dp로 저장하는 것으로 시작

for i in range(1, n):
    temp = []  # 이전 dp값에 현재 값을 더한 값을 저장할 리스트
    min_dp = min(dp)  # 현재 dp의 최솟값
    for j in range(m):
        # 현재 dp의 최솟값이 같은 열이라면 해당 값을 제외한 값 중의 최솟값을 더해서 temp에 추가
        if min(dp) == dp[j]:
            temp_dp = dp.copy()
            del temp_dp[j]
            temp.append(board[i][j] + min(temp_dp))
        # 최솟값이 같은 열이 아니라면 그대로 현재 dp의 최솟값을 더해서 temp에 추가
        else:
            temp.append(board[i][j] + min_dp)

    dp = temp  # i번 인덱스까지의 dp 최신화

print(min(dp))
