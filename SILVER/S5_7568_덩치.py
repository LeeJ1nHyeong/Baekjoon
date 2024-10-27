n = int(input())
stat = [tuple(map(int, input().split())) for _ in range(n)]  # 키와 몸무게를 튜플형태로 저장
rank = [1] * n  # 등수

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        # 키, 몸무게가 둘 다 낮다면 rank 1 추가
        if stat[i][0] < stat[j][0] and stat[i][1] < stat[j][1]:
            rank[i] += 1

print(*rank)
