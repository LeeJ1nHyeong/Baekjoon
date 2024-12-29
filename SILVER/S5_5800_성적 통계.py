k = int(input())

for num in range(1, k + 1):
    n, *score = map(int, input().split())
    score.sort()
    largest_gap = 0

    for i in range(n - 1):
        largest_gap = max(largest_gap, score[i + 1] - score[i])

    print(f"Class {num}")
    print(f"Max {score[-1]}, Min {score[0]}, Largest gap {largest_gap}")
