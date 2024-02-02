from collections import deque

case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    nodes = [[0] * (n + 1) for _ in range(n + 1)]  # 노드 간 간선을 표현하기 위한 2차원 배열
    tree = 0  # 트리의 개수

    # 간선 표시
    for _ in range(m):
        s, e = map(int, input().split())
        nodes[s][e] = 1
        nodes[e][s] = 1

    visited = [0] * (n + 1)  # 방문 표시용

    for i in range(1, n + 1):
        if not visited[i]:
            queue = deque([i])

            cycle = False  # 사이클 존재 여부

            # bfs 진행
            while queue:
                now = queue.popleft()
                if visited[now]:  # 현재 노드가 이전에 방문한 곳이라면 사이클이 존재하므로 True로 바꿈
                    cycle = True

                visited[now] = 1  # 방문 표시

                for i in range(1, n + 1):
                    if nodes[now][i] and not visited[i]:
                        queue.append(i)

            if not cycle:  # 사이클이 존재하지 않다면 트리 개수 1 추가
                tree += 1

    if not tree:
        print(f"Case {case}: No trees.")
    elif tree == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {tree} trees.")

    case += 1