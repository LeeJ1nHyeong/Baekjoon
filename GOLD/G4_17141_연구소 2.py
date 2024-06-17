from collections import deque
from itertools import combinations


# bfs
def bfs(lst):
    global ans

    # 모든 빈칸이 바이러스에 감염됐는지 확인
    def check():
        for i in range(n):
            for j in range(n):
                # 벽은 탐색대상에서 제외
                if lab[i][j] == 1:
                    continue

                # 감염되지 않은 칸이 있다면 False return
                if not visited[i][j]:
                    return False

        return True  # 모든 칸 탐색이 끝났다면 True return

    visited = [[0] * n for _ in range(n)]  # 방문 표시
    queue = deque()

    # 시작좌표를 시간과 함께 튜플형태로 추가 후 방문 표시
    for i, j in lst:
        queue.append((i, j, 0))
        visited[i][j] = 1

    max_day = 0  # 모든 빈칸을 감염시키는 데에 걸린 일
    
    # bfs 진행
    while queue:
        ci, cj, day = queue.popleft()

        max_day = max(day, max_day)

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            
            # 범위를 벗어나면 continue
            if ni < 0 or ni == n or nj < 0 or nj == n:
                continue
            
            # 벽이라면 continue
            if lab[ni][nj] == 1:
                continue
                
            # 방문 지역은 continue
            if visited[ni][nj]:
                continue

            visited[ni][nj] = 1
            queue.append((ni, nj, day + 1))
            
    # 모든 빈 칸을 감염시켰다면 최솟값 여부 확인
    if check():
        ans = min(max_day, ans)


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
virus = []  # 바이러스 위치를 담을 리스트

# 초기값을 n * n으로 설정
ans = n * n

# 바이러스 위치를 리스트에 담기
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus.append((i, j))

# 바이러스 개수 중 m개를 조합하여 bfs 진행
for cv in combinations(virus, m):
    bfs(cv)

# ans가 그대로 n * n이라면 -1 출력, 바뀌었다면 그 값 출력
print(ans if ans != n * n else -1)
