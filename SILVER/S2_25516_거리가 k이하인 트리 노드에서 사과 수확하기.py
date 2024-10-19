from collections import deque

n, k = map(int, input().split())
tree = [[] for _ in range(n)]  # 트리
visited = [0] * n  # 방문 여부

# 노드 간의 간선을 양방향으로 저장
for _ in range(n - 1):
    p, c = map(int, input().split())

    tree[p].append(c)
    tree[c].append(p)

apple = list(map(int, input().split()))  # 사과 위치

# bfs 초기 세팅
cnt = apple[0]
queue = deque([(0, 0)])
visited[0] = 1

# bfs 진행
while queue:
    now, distance = queue.popleft()

    # 루트로부터 거리가 k인 노드라면 continue
    if distance == k:
        continue

    # 현재 노드에서 이동할 수 있는 노드 탐색
    for t in tree[now]:
        # 미방문 노드 탐색
        if not visited[t]:
            # 이동할 노드에 사과가 있다면 cnt 1 추가
            if apple[t]:
                cnt += 1

            # 방문 표시 후 queue에 노드 추가
            visited[t] = 1
            queue.append((t, distance + 1))

print(cnt)
