import sys
input = sys.stdin.readline

def binarySearch(low, high, key):
    if low > high:
        return 0

    mid = (low + high) // 2
    if key == num_list[mid]:
        return 1
    elif key < num_list[mid]:
        return binarySearch(low, mid - 1, key)
    elif key > num_list[mid]:
        return binarySearch(mid + 1, high, key)

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
M = int(input())
find_list = list(map(int, input().split()))

for f in find_list:
    print(binarySearch(0, N - 1, f))