import sys
sys.setrecursionlimit(10**8)  # 재귀 오류 방지

def dfs(i):
    global cnt

    visited[i] = 1
    group.append(i)

    # 다음 차례가 방문되어 있고 group안에 그 번호가 있다면 그 번호의 인덱스 부터 끝까지의 개수만큼 cnt에서 차감
    if visited[choice[i]]:
        if choice[i] in group:
            cnt -= len(group[group.index(choice[i]):])
        return
    
    # 다음 차례가 미방문 되어있다면 재귀 진행
    else:
        dfs(choice[i])

t = int(input())

for _ in range(t):
    n = int(input())
    choice = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)

    cnt = n

    for i in range(1, n + 1):
        if not visited[i]:
            group = []
            dfs(i)

    print(cnt)