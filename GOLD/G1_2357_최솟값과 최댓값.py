import sys
input = sys.stdin.readline


# 최솟값 세그먼트 트리 저장
def min_init(start, end, index):
    if start == end:
        min_segment_tree[index] = numbers[start]
        return min_segment_tree[index]

    mid = (start + end) // 2

    min_segment_tree[index] = min(min_init(start, mid, index * 2),  min_init(mid + 1, end, index * 2 + 1))
    return min_segment_tree[index]


# 최댓값 세그먼트 트리 저장
def max_init(start, end, index):
    if start == end:
        max_segment_tree[index] = numbers[start]
        return max_segment_tree[index]

    mid = (start + end) // 2

    max_segment_tree[index] = max(max_init(start, mid, index * 2),  max_init(mid + 1, end, index * 2 + 1))
    return max_segment_tree[index]


# 구간 별 최솟값 찾기
def interval_min(start, end, index, left, right):
    if left > end or right < start:
        return 1e10

    if left <= start and right >= end:
        return min_segment_tree[index]

    mid = (start + end) // 2
    return min(interval_min(start, mid, index * 2, left, right), interval_min(mid + 1, end, index * 2 + 1, left, right))


# 구간 별 최댓값 찾기
def interval_max(start, end, index, left, right):
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return max_segment_tree[index]

    mid = (start + end) // 2
    return max(interval_max(start, mid, index * 2, left, right), interval_max(mid + 1, end, index * 2 + 1, left, right))


n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
min_segment_tree = [0] * (n * 4)  # 최솟값 세그먼트 트리
max_segment_tree = [0] * (n * 4)  # 최댓값 세그먼트 트리

min_init(0, n - 1, 1)  # 최솟값 세그먼트 트리 저장
max_init(0, n - 1, 1)  # 최댓값 세그먼트 트리 저장

for _ in range(m):
    a, b = map(int, input().split())
    print(interval_min(0, n - 1, 1, a - 1, b - 1), interval_max(0, n - 1, 1, a - 1, b - 1))
