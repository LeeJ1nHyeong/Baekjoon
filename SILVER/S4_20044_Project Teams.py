n = int(input())
student = sorted(list(map(int, input().split())))

ans = student[-1] * 2  # 팀 코딩 역량 합 중 최솟값

# 최소 역량과 최대 역량끼리 합해서 최솟값 여부 확인
for i in range(n):
    w = student[i] + student[2 * n - 1 - i]
    ans = min(ans, w)

print(ans)
