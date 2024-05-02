import sys
input = sys.stdin.readline


def check(a, b):
    # a -> b 방향과 b -> a 방향 최단거리 값을 탐색
    if min_dist[a][b] != 400:  # a -> b의 값이 바뀌었을 경우 -1 return
        return -1
    elif min_dist[b][a] != 400:  # b -> a의 값이 바뀌었을 경우 1 return
        return 1
    else:  # 둘 다 변화가 없을 경우 0 return
        return 0


n, k = map(int, input().split())
min_dist = [[400 for _ in range(n + 1)] for _ in range(n + 1)]  # 각 위치별 최단거리 값을 저장할 2차원 리스트, 문제 조건에 따라 최댓값을 400으로 설정

# 두 사건 간의 거리를 1로 설정
for _ in range(k):
    e1, e2 = map(int, input().split())
    min_dist[e1][e2] = 1

# i번과 j번 간의 거리와 두 사건 사이에 k번을 거쳐서 간 거리 중 최솟값을 저장
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            min_dist[i][j] = min(min_dist[i][j], min_dist[i][k] + min_dist[k][j])

s = int(input())

# 두 사건 간의 전후 관계 탐색
for _ in range(s):
    e1, e2 = map(int, input().split())
    print(check(e1, e2))
