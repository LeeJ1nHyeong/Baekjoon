def check(s, t):  # 문자열 체크
    global ans

    if s == t:  # 두 문자열이 같다면 ans를 1로 바꾸고 종료
        ans = 1
        return
    
    # s가 t에 포함되지 않고, s를 뒤집은 것도 포함되지 않는다면 종료
    if s not in t and s[::-1] not in t:
        return
    
    # 둘 중 하나에 해당된다면 A를 추가한 문자열로 재귀 진행 및 B를 추가하고 뒤집은 문자열로 재귀 진행
    else:
        plus_a = s + 'A'  # 문자열 뒤에 A 추가
        check(plus_a, t)
        plus_b = (s + 'B')[::-1]  # 문자열 뒤에 B 추가 후 뒤집기
        check(plus_b, t)


s = input()
t = input()

ans = 0

check(s, t)

print(ans)