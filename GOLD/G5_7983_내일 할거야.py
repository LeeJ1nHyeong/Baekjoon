import sys
input = sys.stdin.readline


n = int(input())
homework = []

# 필요 일 수(d)와 마감일(t)을 튜플 형태로 리스트에 저장
for _ in range(n):
    d, t = map(int, input().split())
    homework.append((d, t))

# 마감일을 기준으로 내림차순 정렬
homework.sort(key=lambda x: (-x[1], x[0]))

# 가장 늦은 마감일을 변수에 저장
ans = homework[0][1]

# 현재 과제의 마감일과 필요 일 수를 뺀 값과 ans에서 필요 일 수를 뺀 값 중 최솟값을 저장
for d, t in homework:
    ans = min(ans - d, t - d)

print(ans)  # 최솟값 출력
