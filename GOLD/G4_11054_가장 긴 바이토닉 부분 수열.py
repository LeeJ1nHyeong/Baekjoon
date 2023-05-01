import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
reverse_num_list = num_list[::-1]

dp_increase = [1] * N
dp_decrease = [1] * N
dp = [0] * N

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)
        if num_list[N - i - 1] > num_list[N - j - 1]:
            dp_decrease[N - i - 1] = max(dp_decrease[N - i - 1], dp_decrease[N - j - 1] + 1)

for i in range(N):
    dp[i] = dp_increase[i] + dp_decrease[i] - 1

print(max(dp))