from collections import deque

def bfs(i):  # bfs
    global visited

    cnt = 0  # 리프노드 개수

    # bfs 초기 설정
    queue = deque()
    queue.append(i)
    visited[i] = 1

    # bfs 진행
    while queue:
        now = queue.popleft()

        leaf_node = False  # 리프노드 여부
        if not nodes[now]:  # 자식 노드가 없다면 leaf_node를 True로 변경
            leaf_node = True
        # 자식 노드가 있을 경우
        else:
            node_cnt = 0  # 노드 개수
            for node in nodes[now]:
                if not visited[node]:  # 미방문 노드가 있다면 queue에 추가
                    node_cnt += 1
                    visited[node] = 1
                    queue.append(node)

            if not node_cnt:  # 미방문 노드 개수가 없다면 leaf_node를 True로 변경
                leaf_node = True

        if leaf_node:  # 리프노드라면 cnt 1 추가
            cnt += 1

    return cnt  # bfs 종료 후 리프노드 개수 return


n = int(input())
nodes = [[] for _ in range(n)]
lines = list(map(int, input().split()))
remove_node = int(input())

# 노드 간 간선 표시
for i in range(n):
    if lines[i] == -1:
        continue
    else:
        nodes[lines[i]].append(i)

cnt = 0
visited = [0] * n  # 노드 방문 여부

bfs(remove_node)  # 제거시킬 노드부터 bfs 진행하여 방문 표시 진행

for i in range(n):
    if lines[i] == -1 and i != remove_node:  # 부모노드가 없고 제거할 노드가 아니라면 bfs 진행
        cnt += bfs(i)

print(cnt)