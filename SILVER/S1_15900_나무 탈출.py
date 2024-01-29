n = int(input())
tree = [[] for _ in range(n + 1)]  # 트리
visited = [0] * (n + 1)  # 방문 표시용
cnt = 0

# dfs 초기 작업
stack = [(1, 0)]  # (노드 번호, 깊이값)
visited[1] = 1

# 노드 간선 표시
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# dfs 진행
while stack:
    now, depth = stack.pop()
    tree_node = False  # 리프 노드 유무

    for node in tree[now]:
        # 현재 노드와 연결된 노드 중 미방문 노드라면 리프 노드라는 뜻이므로 True로 바꾼 뒤 스택에 추가
        if not visited[node]:
            tree_node = True
            visited[node] = 1
            stack.append((node, depth + 1))

    if not tree_node:  # 리프 노드가 없다면 깊이값을 더해줌
        cnt += depth

# 홀수일 경우 성원 승리(Yes), 짝수일 경우 성원 패배(No)
if cnt % 2:
    print("Yes")
else:
    print("No")