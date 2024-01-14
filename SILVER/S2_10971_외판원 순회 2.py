def backtrack(start, i, visited, cnt, cost):  # 백트래킹
    global min_cost

    # 모든 번호 순회를 완료 했을 경우 최소비용값을 저장하고 종료
    if cnt == n: 
        if city[i][start]:  # 처음으로 돌아가는 비용이 0이 아닐 경우에만 진행
            cost += city[i][start]
            min_cost = min(cost, min_cost)
        return

    if cost >= min_cost:  # 순회 진행 중에 최솟값을 넘길 경우 자동 종료
        return

    for j in range(n):
        if i != j and city[i][j] and not visited[j]:
            visited[j] = 1
            backtrack(start, j, visited, cnt + 1, cost + city[i][j])
            visited[j] = 0

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
min_cost = 1000000 * n  # 최솟값

for i in range(n):
    visited = [0] * n
    visited[i] = 1
    backtrack(i, i, visited, 1, 0)

print(min_cost)