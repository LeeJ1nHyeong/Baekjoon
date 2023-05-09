import sys
input = sys.stdin.readline

def makePartSum(i, j, partSum, lst):
    global cnt
    if i == j:
        return

    for k in range(i, j):
        partSum += num_list[k]
        if partSum == S:
            cnt += 1
        lst.append(partSum)
        makePartSum(k + 1, j, partSum, lst)
        partSum -= num_list[k]

def binarySearch(start, end, key):
    global cnt

    if start > end:
        return

    middle = (start + end) // 2

    if sum_B[middle] == key:
        cnt += temp[key]
        return

    elif sum_B[middle] > key:
        return binarySearch(start, middle - 1, key)
    else:
        return binarySearch(middle + 1, end, key)

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
sum_A = []
sum_B = []
cnt = 0

mid = N // 2

makePartSum(0, mid, 0, sum_A)
makePartSum(mid, N, 0, sum_B)
sum_B.sort()
temp = {}

for b in sum_B:
    if b in temp:
        temp[b] = temp[b] + 1
    else:
        temp[b] = 1

for A in sum_A:
    key = S - A
    left, right = 0, len(sum_B) - 1
    while left <= right:
        middle = (left + right) // 2

        if sum_B[middle] == key:
            cnt += temp[key]
            break

        elif sum_B[middle] > key:
            right = middle - 1
        else:
            left = middle + 1

print(cnt)