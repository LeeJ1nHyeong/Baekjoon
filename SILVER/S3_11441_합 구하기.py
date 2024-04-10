import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
sum_list = [0] * (n + 1)  # i번째 숫자까지의 누적 합을 구현할 리스트

# i번 인덱스까지의 누적 합 저장
for i in range(n):
    sum_list[i + 1] = sum_list[i] + numbers[i]

# j번째 누적 합에서 i - 1번째 누적 합을 뺀 값을 출력
m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    ans = sum_list[j] - sum_list[i - 1]
    print(ans)
