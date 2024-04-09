def dfs(num, depth):
    global ans

    # 친구의 친구까지 탐색
    if depth > 2:
        return
    
    # 미방문 지역에 대해 방문 표시 후 ans 1 추가 뒤 dfs 진행
    for node in nodes[num]:
        if not visited[node]:
            visited[node] = 1
            ans += 1
        dfs(node, depth + 1)


n = int(input())
m = int(input())
nodes = [[] for _ in range(n + 1)]  # 노드 간 간선을 구현할 2차원 리스트
visited = [0] * (n + 1)  # 방문 표시용 리스트
ans = 0  # 결혼식 초대 인원

# 노드 간 간선 표시
for _ in range(m):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)

# root 방문 표시 후 dfs 진행
visited[1] = 1
dfs(1, 1)  # depth 1로 시작

print(ans)  # 결혼식 초대 인원 출력
