na, nb = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

b_hash = {}  # b의 숫자를 담을 해쉬

# b의 숫자를 해쉬에 추가
for b in b_list:
    b_hash[b] = 1

ans = []

# try-except 문을 활용하여 a에는 있지만 b에는 없는 숫자를 분류
for a in a_list:
    try:
        if b_hash[a]:
            continue
    # KeyError가 발생한다면 ans에 숫자 추가
    except KeyError:
        ans.append(a)

print(len(ans))  # ans의 길이 출력
# ans에 숫자가 있다면 오름차순 정렬 후 원소 출력
if ans:
    ans.sort()
    print(*ans)
