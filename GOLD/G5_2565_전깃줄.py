n = int(input())
lines = []
dp = [1] * n

# 전깃줄의 시작점, 끝점을 튜플 형태로 리스트에 저장
for _ in range(n):
    s, e = map(int, input().split())
    lines.append((s, e))

lines.sort()  # 시작점을 기준으로 오름차순 정렬

# 각 전깃줄보다 시작점이 작은 전깃줄과 비교하여 끝점이 더 작은 전깃줄이 최대로 이어지는 값을 dp에 저장
for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))  # 전체 전깃줄 개수에서 dp값의 최댓값을 뺀 값을 출력
