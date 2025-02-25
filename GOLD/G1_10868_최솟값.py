import sys
input = sys.stdin.readline


# 세그먼트 트리 최솟값 저장
def init(start, end, index):
    if start == end:
        segment_tree[index] = numbers[start]
        return segment_tree[index]

    mid = (start + end) // 2

    segment_tree[index] = min(init(start, mid, index * 2),  init(mid + 1, end, index * 2 + 1))
    return segment_tree[index]


# 구간 별 최솟값 찾기
def interval_min(start, end, index, left, right):
    # 구간 범위를 벗어나면 큰 수(1e10) return
    if left > end or right < start:
        return 1e10
    
    # 현재 구간이 범위 내에 포함되어 있다면 현재 구간의 최솟값 return
    if left <= start and right >= end:
        return segment_tree[index]
    
    mid = (start + end) // 2
    return min(interval_min(start, mid, index * 2, left, right), interval_min(mid + 1, end, index * 2 + 1, left, right))


n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
segment_tree = [0] * (n * 4)

# 세그먼트 트리에 구간별 최솟값 저장
init(0, n - 1, 1)

# a ~ b 구간의 최솟값 출력
for _ in range(m):
    a, b = map(int, input().split())
    print(interval_min(0, n - 1, 1, a - 1, b - 1))
