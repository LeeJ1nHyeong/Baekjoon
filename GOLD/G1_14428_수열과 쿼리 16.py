import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        segment_tree[index] = start
        return segment_tree[index]

    mid = (start + end) // 2

    left = init(start, mid, index * 2)
    right = init(mid + 1, end, index * 2 + 1)

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


# 구간 별 최솟값의 인덱스 탐색
def interval_min(start, end, index, left, right):
    # 범위가 탐색 구간을 벗어날 경우 탐색구간의 최소 인덱스를 return
    if left > end or right < start:
        return left

    if left <= start and right >= end:
        return segment_tree[index]

    mid = (start + end) // 2

    l = interval_min(start, mid, index * 2, left, right)
    r = interval_min(mid + 1, end, index * 2 + 1, left, right)

    if a[l] <= a[r]:
        return l
    else:
        return r


n = int(input())
a = list(map(int, input().split()))
m = int(input())

segment_tree = [0] * (n * 4)

# 세그먼트 트리에 구간 별 최솟값의 인덱스 저장
init(0, n - 1, 1)

for _ in range(m):
    q, *num = map(int, input().split())

    # 특정 인덱스의 숫자 변경 후 세그먼트 트리 최신화
    if q == 1:
        i, v = num
        a[i - 1] = v
        change_value(0, n - 1, 1, i - 1, v)

    # 탐색할 구간의 최솟값 인덱스 출력
    else:
        i, j = num
        print(interval_min(0, n - 1, 1, i - 1, j - 1) + 1)
