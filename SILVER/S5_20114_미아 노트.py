n, h, w = map(int, input().split())
word = [list(input()) for _ in range(h)]
ans = ""

for k in range(n):
    find = "?"  # 탐색 범위에서 찾은 문자
    # 탐색 범위 내에 알파벳이 있다면 해당 문자를 ans에 추가, 없다면 "?"를 추가
    for i in range(h):
        for j in range(w * k, w * (k + 1)):
            if word[i][j] != "?":
                find = word[i][j]

    ans += find

# 찾은 문자열 출력
print(ans)
