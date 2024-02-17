def backtrack(i, total, cnt, visited):  # 백트래킹
    global max_total

    if cnt == n:  # 모든 수를 다 사용했을 경우 최댓값 여부 판별
        max_total = max(total, max_total)
        return

    for j in range(n):
        if not visited[j]:  # 사용하지 않은 수를 골라 현재 값과의 차이의 절댓값을 더해주고 백트래킹
            visited[j] = 1
            backtrack(j, total + abs(num_list[i] - num_list[j]), cnt + 1, visited)
            visited[j] = 0


n = int(input())
num_list = list(map(int, input().split()))

max_total = 0  # 최댓값
visited = [0] * n  # 방문 표시용

for i in range(n):
    visited[i] = 1
    backtrack(i, 0, 1, visited)
    visited[i] = 0

print(max_total)