import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        segment_tree[index] = numbers[start] % 1000000007
        return segment_tree[index]

    mid = (start + end) // 2
    segment_tree[index] = (init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1)) % 1000000007
    return segment_tree[index]


def change_value(start, end, index, node, value):
    if node < start or node > end:
        return segment_tree[index]

    if start == end:
        segment_tree[index] = value
        return value

    mid = (start + end) // 2

    segment_tree[index] = change_value(start, mid, index * 2, node, value) * change_value(mid + 1, end, index * 2 + 1, node, value) % 1000000007
    return segment_tree[index]


def interval_multiply(start, end, index, left, right):
    if left > end or right < start:
        return 1

    if left <= start and right >= end:
        return segment_tree[index] % 1000000007

    mid = (start + end) // 2
    return (interval_multiply(start, mid, index * 2, left, right) * interval_multiply(mid + 1, end, index * 2 + 1, left, right)) % 1000000007


n, m, k = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
segment_tree = [0] * (n * 4)

init(0, n - 1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        change_value(0, n - 1, 1, b - 1, c)
        numbers[b - 1] = c

    else:
        print(int(interval_multiply(0, n - 1, 1, b - 1, c - 1)))
