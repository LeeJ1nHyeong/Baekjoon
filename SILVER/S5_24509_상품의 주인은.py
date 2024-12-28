import sys
input = sys.stdin.readline

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]

ans = []

for i in range(1, 5):
    number = 200001
    max_score = -1
    for j in range(n):
        if score[j][0] in ans:
            continue

        if score[j][i] > max_score:
            number = score[j][0]
            max_score = score[j][i]

        elif score[j][i] == max_score:
            number = min(number, score[j][0])

    ans.append(number)

print(*ans)
