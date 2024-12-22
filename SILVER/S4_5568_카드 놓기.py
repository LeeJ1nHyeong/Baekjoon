n = int(input())
k = int(input())
numbers = [int(input()) for _ in range(n)]
new_numbers = set()


# 백트래킹 (4716 ms)
def backtrack(cnt, num):
    if cnt == k:
        new_numbers.add(int(num))

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            backtrack(cnt + 1, num + str(numbers[i]))
            visited[i] = 0

visited = [0] * n

for i in range(n):
    visited[i] = 1
    backtrack(1, str(numbers[i]))
    visited[i] = 0

print(len(new_numbers))


# 라이브러리 itertools 이용 (44 ms)
import itertools

for i in list(itertools.permutations(numbers, k)):
    new_numbers.add("".join(map(str, i)))

print(len(new_numbers))
