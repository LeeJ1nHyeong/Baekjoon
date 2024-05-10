n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# i에서 j로 가는 경로에서 중간에 k를 거쳐가는 경로가 있다면 (i, j) 좌표 1로 변경
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# 형식에 맞게 출력
for g in graph:
    print(*g)
