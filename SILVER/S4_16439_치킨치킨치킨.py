n, m = map(int, input().split())
favorite = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 치킨 3개를 선택
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            score = 0

            # 각 회원별 고른 치킨의 선호도 중 최댓값을 score에 추가
            for f in favorite:
                score += max(f[i], f[j], f[k])

            # 최댓값 여부 확인
            ans = max(ans, score)

print(ans)
