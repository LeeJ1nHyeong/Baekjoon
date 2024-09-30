n, m = map(int, input().split())
max_m = []  # 각 과목별 사용할 마일리지 최솟값

for _ in range(n):
    p, l = map(int, input().split())
    # 각 과목별 수강신청에 사용한 마일리지를 내림차순으로 정렬
    p_m = sorted(list(map(int, input().split())), reverse=True)

    # 수강 신청 인원이 정원보다 작으면 1을 max_m에 추가
    if len(p_m) < l:
        max_m.append(1)

    # 수강 신청 인원이 정원보다 크거나 같으면 max_m에 수강 정원 수에 해당하는 마일리지 값을 max_m에 추가
    else:
        max_m.append(p_m[l - 1])

# max_m 오름차순 정렬
max_m.sort()

# 갖고 있는 마일리지 이내에서 수강 신청 가능한 과목 개수 계산 후 출력
ans = 0
use_m = 0
for i in range(n):
    if use_m + max_m[i] > m:
        break

    use_m += max_m[i]
    ans += 1

print(ans)
