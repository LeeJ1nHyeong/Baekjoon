n = int(input())
time = []

# 필요 시간(t), 마감 시간(s)를 튜플 형태로 리스트에 저장
for _ in range(n):
    t, s = map(int, input().split())
    time.append((t, s))

# 마감 시간이 늦은 일을 기준으로 내림차순 정렬
time.sort(key=lambda x: (-x[1], x[0]))

ans = time[0][1]  # 가장 늦은 마감 시간을 변수에 저장
for t, s in time:
    # 현재 일의 마감 시간과 필요 시간을 뺀 값과 ans에서 필요 시간을 뺀 값 중 최솟값을 저장
    ans = min(s - t, ans - t)
    # 이 때 최솟값이 0 미만이라면 -1로 변경 후 for문 종료
    if ans < 0:
        ans = -1
        break

print(ans)