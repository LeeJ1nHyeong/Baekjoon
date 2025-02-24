import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        segment_tree[index] = numbers[start]
        return segment_tree[index]

    mid = (start + end) // 2
    segment_tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)

    return segment_tree[index]


def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return segment_tree[index]

    mid = (start + end) // 2

    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)


def change_value(start, end, index, node, value):
    if node > end or node < start:
        return

    segment_tree[index] += value

    if start == end:
        return

    mid = (start + end) // 2
    change_value(start, mid, index * 2, node, value)
    change_value(mid + 1, end, index * 2 + 1, node, value)


n, q = map(int, input().split())
numbers = list(map(int, input().split()))
segment_tree = [0] * (n * 4)

# 세그먼트 트리에 구간 합 저장
init(0, n - 1, 1)

for _ in range(q):
    x, y, a, b = map(int, input().split())

    # x > y인 경우도 있기 때문에 min, max 활용
    print(interval_sum(0, n - 1, 1, min(x - 1, y - 1), max(x - 1, y - 1)))

    # 구간 합 계산 후 값 변경
    change_value(0, n - 1, 1, a - 1, b - numbers[a - 1])
    numbers[a - 1] = b

