N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]
one_count = 0
for _ in range(N):
    x, y = map(int,input().split())
    for a in range(x, x+10):
        for b in range(y, y+10):
            if paper[a][b] == 1:
                continue
            else:
                paper[a][b] = 1

for a in range(101):
    for b in range(101):
        if paper[a][b] == 1:
            one_count += 1

print(one_count)