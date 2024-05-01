from collections import deque
import sys
input = sys.stdin.readline


def bfs(start, end, v):
    global ans

    # bfs 초기 설정
    v[start] = 1
    queue = deque()
    queue.append((start, [start]))  # 정점과 방문 노드 리스트를 튜플 형태로 queue에 추가

    # bfs 진행
    while queue:
        now, node_list = queue.popleft()

        # 현재 노드와 간선으로 연결된 노드 탐색
        for node in nodes[now]:
            # 다음 노드가 도착점일 경우
            if node == end:
                # 도착점이 e일 경우
                if end == e:
                    ans += len(node_list)  # ans에 방문한 노드 개수를 더해주기
                    # 최단경로로 이동한 노드들을 새로 방문 표시 후 return
                    v = [0] * (n + 1)
                    for nl in node_list:
                        v[nl] = 1
                    return v
                
                # 도착점이 s일 경우 e를 포함한 방문 노드 개수 return
                return len(node_list)
            
            # 미방문 노드를 탐색 후 queue에 추가
            if not v[node]:
                v[node] = 1
                queue.append((node, node_list + [node]))


n, m = map(int, input().split())
nodes = [[] for _ in range(n + 1)]  # 노드 간의 간선을 저장할 2차원 리스트
visited = [0] * (n + 1)  # 방문 여부 표시용 리스트
ans = 0

# 노드 간의 간선 정보를 양방향으로 저장
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

# 방문 노드 개수가 같을 경우 사전순으로 가장 빠른 길을 찾으므로 각 노드에 연결된 노드 리스트를 오름차순으로 정렬
for node in nodes:
    node.sort()

s, e = map(int, input().split())

visited = bfs(s, e, visited)  # s -> e 방향 bfs 진행
ans += bfs(e, s, visited)  # e -> s 방향 bfs 진행

print(ans)  # 최단 거리 출력
