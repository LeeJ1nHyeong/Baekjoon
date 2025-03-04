n = int(input())
a = list(map(int, input().split()))
sort_a = sorted(a)
p = []

for i in range(n):
    # 정렬된 수열의 인덱스 값을 p에 저장
    p.append(sort_a.index(a[i]))

    # 중복 방지를 위해 해당 인덱스의 숫자를 -1로 변경
    sort_a[sort_a.index(a[i])] = -1

print(*p)
