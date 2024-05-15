n = int(input())
x_list = []

for _ in range(n):
    x_list.append(input())

x_list.sort(key=lambda x: len(x))  # 문자열 길이 순서대로 오름차순 정렬

cnt = 0  # 부분 집합 최대 크기

# i번째 문자열을 기준으로 뒤의 문자열의 접두어 여부 확인
for i in range(n):
    target = x_list[i]

    check = True  # 접두사 여부 체크
    for j in range(i + 1, n):
        # 뒤 문자열의 접두어가 i번째 문자열이라면 check를 False로 바꾼 후 for문 종료
        if x_list[j][:len(target)] == target:
            check = False
            break

    # 접두어인 문자열이 없을 경우 cnt 1 추가
    if check:
        cnt += 1

print(cnt)  # 부분 집합 최대 크기 출력
