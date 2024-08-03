import sys
input = sys.stdin.readline

n, q = map(int, input().split())

# 수열 비오름차순 정렬
num_list = sorted(list(map(int, input().split())))

# 누적 합 리스트 생성
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + num_list[i - 1]

# 문제 범위에 해당하는 누적 합을 계산하여 출력
for _ in range(q):
    s, e = map(int, input().split())
    ans = dp[e] - dp[s - 1]
    print(ans)
