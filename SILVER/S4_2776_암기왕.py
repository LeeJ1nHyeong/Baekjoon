# 이진 탐색
def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        # 찾는 숫자가 있다며 1 return
        if note1[mid] == target:
            return 1

        if note1[mid] < target:
            start = mid + 1
        elif note1[mid] > target:
            end = mid - 1

    return 0  # 찾는 숫자가 없다면 0 출력


t = int(input())

for _ in range(t):
    n = int(input())

    # 노트1의 숫자를 오름차순 정렬 상태로 저장
    note1 = sorted(list(map(int, input().split())))
    m = int(input())
    note2 = list(map(int, input().split()))

    # 이진 탐색 진행
    for i in range(m):
        print(binary_search(0, n - 1, note2[i]))


# 해쉬
t = int(input())

for _ in range(t):
    n = int(input())
    
    # 노트1의 숫자들을 set에 저장
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    # 노트2의 숫자가 노트1에 있다면 1, 없다면 0을 출력
    for i in range(m):
        print(1 if note2[i] in note1 else 0)
