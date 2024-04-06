s = input()

part_s = set()  # 부분 문자열을 담을 집합

# i번 인덱스부터 j번 인덱스까지의 부분 문자열을 집합에 추가
# 집합이므로 중복은 자동으로 제거
for i in range(len(s)):
    for j in range(i, len(s)):
        part_s.add(s[i:j + 1])

print(len(part_s))