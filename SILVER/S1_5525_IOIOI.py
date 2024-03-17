n = int(input())
m = int(input())
s = input()

ans, idx, cnt = 0, 0, 0  # P_N의 개수, 현재 인덱스, OI 개수

while idx < m - 1:
    if s[idx : idx + 3] == "IOI":  # 현재 idx부터 문자열 3개가 "IOI"라면
        idx += 2  # idx 2 추가
        cnt += 1  # cnt 1 추가
        if cnt == n:  # cnt가 n이라면 P_N이 성립하므로 ans 1 추가
            ans += 1
            cnt -= 1

    else:  # 아니라면 다음 idx로 이동
        idx += 1
        cnt = 0

print(ans)