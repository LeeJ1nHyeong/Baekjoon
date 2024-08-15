n = int(input())
m = int(input())
material = sorted(list(map(int, input().split())))  # 재료 오름차순 정렬

cnt = 0  # 만들 수 있는 갑옷 개수

# 최솟값과 최댓값을 투 포인터로 지정한 상태로 시작
i, j = 0, n - 1

while i < j:
    # 두 재료의 합이 크거나 같을 경우 j를 한 칸 뒤로 이동
    if material[i] + material[j] >= m:
        # 이 때 두 재료의 합이 m일 경우 cnt 1 추가
        if material[i] + material[j] == m:
            cnt += 1
        j -= 1

    # 두 재료의 합이 작을 경우 i를 한 칸 앞으로 이동
    else:
        i += 1

# 만들 수 있는 갑옷의 개수 출력
print(cnt)
