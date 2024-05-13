import sys
input = sys.stdin.readline

s = input()
q = int(input())

alphabet = {}  # 각 알파벳 별 누적 합을 저장할 딕셔너리

# 각 문자열의 누적합을 alphabet에 저장
for i in range(len(s)):
    if s[i] not in alphabet:
        sum_list = [0] * (len(s) + 1)

        for j in range(1, len(s) + 1):
            if s[j - 1] == s[i]:
                sum_list[j] = sum_list[j - 1] + 1
            else:
                sum_list[j] = sum_list[j - 1]

        alphabet[s[i]] = sum_list

# 질문으로 제시한 구간 내 문자의 개수를 출력
for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)

    # alphabet 내에 문자가 없다면 0 출력
    if a not in alphabet:
        print(0)
    else:
        print(alphabet[a][r + 1] - alphabet[a][l])
