n, k = map(int, input().split())
medal = [list(map(int, input().split())) for _ in range(n)]

medal.sort(key=lambda x: (-x[1], -x[2], -x[3]))
rank, tie = 1, 0

for i in range(n):
    if i != 0:
        if medal[i - 1][1:] == medal[i][1:]:
            tie += 1
        else:
            if tie:
                rank += tie
                tie = 0
            rank += 1

    if medal[i][0] == k:
        break

print(rank)
