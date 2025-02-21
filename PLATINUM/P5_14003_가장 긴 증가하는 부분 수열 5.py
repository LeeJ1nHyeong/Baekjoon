def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if partial[mid] == target:
            return mid
        elif partial[mid] < target:
            start = mid + 1
        elif partial[mid] > target:
            end = mid - 1

    return start


n = int(input())
numbers = list(map(int, input().split()))

partial = [numbers[0]]  # 최장 증가 부분 수열 리스트
dp = [(numbers[0], 0)]  # 이진 탐색을 통해 몇번째 순서에 기록될 지를 저장하는 dp

# 이진 탐색으로 최장 증가 부분 수열 인덱스를 구하면서 dp에 함께 저장
for i in range(n):
    if numbers[i] > partial[-1]:
        partial.append(numbers[i])
        dp.append((numbers[i], len(partial) - 1))

    else:
        idx = binary_search(0, len(partial) - 1, numbers[i])
        partial[idx] = numbers[i]
        dp.append((numbers[i], idx))

# dp 리스트를 활용하여 역추적을 진행하면서 최장 증가 부분 수열 탐색
now = len(partial) - 1
ans = []
for i in range(n, -1, -1):
    if now < 0:
        break

    if dp[i][1] == now:
        ans.append(dp[i][0])
        now -= 1

ans.reverse()
print(len(partial))
print(*ans)
