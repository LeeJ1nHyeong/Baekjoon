import sys
input = sys.stdin.readline


# 세그먼트 트리 생성
def init(start, end, index):
    if start == end:
        segment_tree[index] = numbers[start]
        return segment_tree[index]

    mid = (start + end) // 2

    # 각 세그먼트 트리의 노드 값을 분할 정복으로 저장
    segment_tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return segment_tree[index]


# 구간 합 구하기
def interval_sum(start, end, index, left, right):
    # 범위를 벗어나면 0 return
    if left > end or right < start:
        return 0

    # 범위 내에 포함되어 있는 구간이라면 세그먼트 트리에 저장되어 있는 구간 합 return
    if left <= start and right >= end:
        return segment_tree[index]

    mid = (start + end) // 2

    # 분할 정복으로 구간 합 return
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)


# 값 변경
def change_value(start, end, index, node, value):
    # 변경할 노드가 범위 밖이라면 return
    if node < start or node > end:
        return

    # 변경할 값이 포함되어있는 구간 합에 추가
    segment_tree[index] += value

    # 단일 구간 노드라면 return
    if start == end:
        return

    mid = (start + end) // 2

    # 재귀를 활용하여 수정할 구간 합 노드 탐색
    change_value(start, mid, index * 2, node, value)
    change_value(mid + 1, end, index * 2 + 1, node, value)


n, m, k = map(int, input().split())
segment_tree = [0] * (n * 4)
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

init(0, len(numbers) - 1, 1)  # 세그먼트 트리 생성

for _ in range(m + k):
    a, b, c = map(int, input().split())
    
    # a가 1이라면 (b - 1)번 인덱스 값을 변경한 후 구간 합 수정
    if a == 1:
        change_value(0, len(numbers) - 1, 1, b - 1, c - numbers[b - 1])
        numbers[b - 1] = c
        
    # a가 2라면 구간 (b - 1) ~ (c - 1)에 해당하는 구간 합 출력
    else:
        print(interval_sum(0, len(numbers) - 1, 1, b - 1, c - 1))
