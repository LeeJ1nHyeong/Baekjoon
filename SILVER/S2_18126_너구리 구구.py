from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# 노드 간 간선을 양방향으로 저장
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

ans = 0  # 최대 이동 거리

# bfs 초기 세팅
queue = deque([(1, 0)])  # 현재 위치와 이동 거리를 튜플 형태로 저장
visited[1] = 1

# bfs 진행
while queue:
    now, distance = queue.popleft()

    # 현재 이동 거리의 최댓값 여부 확인
    ans = max(ans, distance)

    # 현재 위치에서 다음 이동 지역 탐색
    for next_node, d in tree[now]:
        # 미방문 지역에 대해 방문 표시 후 queue에 추가
        if not visited[next_node]:
            visited[next_node] = 1
            queue.append((next_node, distance + d))

print(ans)  # 최대 이동 거리 출력
