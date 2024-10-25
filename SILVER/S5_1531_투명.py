n, m = map(int, input().split())
paper = [[0] * 100 for _ in range(100)]  # 100x100 종이

# 불투명 종이로 제시한 범위를 가림
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            paper[i][j] += 1

cnt = 0

# 덮혀진 종이 개수가 m개를 넘길 경우 cnt 1 추가
for i in range(100):
    for j in range(100):
        if paper[i][j] > m:
            cnt += 1

print(cnt)
