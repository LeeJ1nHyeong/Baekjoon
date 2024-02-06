def backtrack(now, visited, cnt):  # 백트래킹
    global ans

    if cnt == 5:  # 연속으로 방문한 노드 개수가 5개라면 ans를 1로 바꾸고 백트래킹 종료
        ans = 1
        return
    
    # 다음 노드에 미방문한 노드가 있는지 확인
    for node in nodes[now]:
        if not visited[node]:
            visited[node] = 1
            backtrack(node, visited, cnt + 1)
            visited[node] = 0

n, m = map(int, input().split())
nodes = [[] for _ in range(n + 1)]  # 노드간의 간선을 표시하기 위한 2차원 배열

# 노드 간선 표시
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [0] * (n + 1)  # 방문 표시용

ans = 0
# 방문하지 않은 노드를 시작점으로하여 백트래킹 진행
for i in range(1, n + 1):
    visited[i] = 1
    backtrack(i, visited, 1)
    visited[i] = 0

print(ans)