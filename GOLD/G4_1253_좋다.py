n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()  # 오름차순 정렬

cnt = 0

for i in range(n):
    target = num_list[i]  
    l, r = 0, n - 1  # 양 끝에서 투 포인터 시작

    # 투 포인터
    while l < r:
        # target에 해당하는 숫자를 사용하지 않도록 포인터 조정
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        s = num_list[l] + num_list[r]  # 두 수의 합
        if s == target:  # 두 수의 합이 target이라면  cnt 1 추가 후 while문 종료
            cnt += 1
            break
        elif s > target:  # 두 수의 합이 target보다 크다면 오른쪽 인덱스 1 감소
            r -= 1
        else:  # 두 수의 합이 target보다 작다면 왼쪽 인덱스 1 증가
            l += 1

print(cnt)