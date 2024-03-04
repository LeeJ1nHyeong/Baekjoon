s = list(input())  # 처음 문자열
t = list(input())  # 만들고 싶은 문자열

# t 문자열의 마지막 문자를 pop시키면서 s와 길이가 같아질 때까지 진행
while len(s) != len(t):
    if t.pop() == "B":  # 마지막 문자가 B라면 문자열 뒤집기
        t = t[::-1]

# 문자열 제거 진행 후 s와 t가 같다면 1 출력, 다르다면 0 출력
if s == t:
    print(1)
else:
    print(0)