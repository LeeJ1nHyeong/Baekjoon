# KMP 알고리즘을 활용한 풀이

t = list(input())
p = list(input())

pi = [0 for _ in range(len(p))]  # 패턴 내 접두, 접미 부분 문자열이 최대로 같은 값을 담기위한 pi 배열

i = 0  # pi 배열 인덱스
for j in range(1, len(p)):
    while i > 0 and p[i] != p[j]:  # 다른 문자가 나올 때 까지 인덱스의 값을 pi[i - 1]으로 설정
        i = pi[i - 1]
    if p[i] == p[j]:  # 같은 문자열일 경우 i를 1 증가시키고 그 값을 pi의 j 인덱스에 저장
        i += 1
        pi[j] = i

idx_list = []  # 문자열의 시작 인덱스를 담을 리스트
idx = 0  # 문자열 비교를 위한 인덱스
for k in range(len(t)):
    while idx > 0 and p[idx] != t[k]:  # pi 배열을 활용하여 인덱스 설정
        idx = pi[idx - 1]

    if p[idx] == t[k]:  # 같은 문자열일 경우 인덱스 1 증가
        idx += 1
        if idx == len(p):  # 패턴이 존재함을 확인한다면 해당 부분의 시작 인덱스를 리스트에 추가
            idx_list.append(k - idx + 2)
            idx = pi[idx - 1]

print(len(idx_list))
print(*idx_list)