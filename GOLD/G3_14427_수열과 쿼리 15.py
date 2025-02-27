import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        segment_tree[index] = start
        return segment_tree[index]

    mid = (start + end) // 2

    left = init(start, mid, index * 2)
    right = init(mid + 1, end, index * 2 + 1)

    # 두 숫자 중 더 작은 숫자의 인덱스를 세그먼트 트리에 저장
    # 같다면 left를 저장 (항상 left가 작은 인덱스 값임을 보장할 수 있음)
    if a[left] <= a[right]:
        segment_tree[index] = left
    else:
        segment_tree[index] = right

    return segment_tree[index]


def change_value(start, end, index, node, value):
    if node < start or node > end:
        return segment_tree[index]

    if start == end:
        segment_tree[index] = node
        return segment_tree[index]

    mid = (start + end) // 2

    left = change_value(start, mid, index * 2, node, value)
    right = change_value(mid + 1, end, index * 2 + 1, node, value)

    if a[left] <= a[right]:
        segment_tree[index] = left
    else:
        segment_tree[index] = right

    return segment_tree[index]


n = int(input())
a = list(map(int, input().split()))
m = int(input())

segment_tree = [0] * (n * 4)

init(0, n - 1, 1)

for _ in range(m):
    q, *num = map(int, input().split())

    if q == 1:
        i, v = num
        a[i - 1] = v
        change_value(0, n - 1, 1, i - 1, v)

    else:
        print(segment_tree[1] + 1)
