N = int(input())
t_list = []
p_list = []

dp = [0] * (N + 1)

for i in range(N):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

for i in range(N):
    for j in range(i + t_list[i], N + 1):
        if dp[j] < dp[i]  + p_list[i]:
            dp[j] = dp[i]  + p_list[i]

print(dp[-1])