target = input()
n = int(input())

ans = 0
for _ in range(n):
    # 반지에 각인된 문자열의 뒤에 target 글자수에서 1을 뺀 값 만큼 각인 문자열의 앞 글자들을 뒤에 추가
    ring = input()
    ring += ring[:len(target) - 1]

    # target 문자열이 존재한다면 ans 1 추가
    if target in ring:
        ans += 1

# 문자열이 들어있는 반지 개수 출력
print(ans)
