def bubble_sort():
    # 버블 정렬 진행 전에 이미 두 배열 순서가 같은 경우 1 return
    if check(a, b):
        return 1
    
    # 버블 정렬 진행
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

                # 버블 정렬 교환 후 (j + 1)번 인덱스가 같은 값이 됐다면 두 배열이 같은 순서인지 확인
                if a[j + 1] == b[j + 1]:
                    if check(a, b):
                        return 1

    return 0


def check(l1, l2):
    for i in range(n):
        if l1[i] != l2[i]:
            return False

    return True


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(bubble_sort())
