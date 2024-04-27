from collections import deque


def bfs():
    # 초기 설정
    queue = deque([n])
    # 시작 좌표와 걸린 시간을 설정
    visited[n] = n
    dist[n] = 0

    # bfs 진행
    while queue:
        now = queue.popleft()

        # 현재 좌표가 도착점이라면 이동 시간을 출력 후 방문 좌표를 리스트로 만들어 출력
        if now == k:
            print(dist[now])

            # 방문 지역을 변수를 활용하여 역추적하면서 리스트에 추가
            move_list = [k]
            idx = k
            while idx != n:
                move_list.append(visited[idx])
                idx = visited[idx]
            
            # 리스트 추가 후 역순으로 뒤집어서 출력
            move_list.reverse()
            print(*move_list)
            return
        
        # 0에서 100000 사이의 값 중 이동 가능한 미방문 지역을 찾아 queue에 추가
        for target in (now - 1, now + 1, 2 * now):
            if 0 <= target <= 100000 and visited[target] == -1:
                dist[target] = dist[now] + 1
                visited[target] = now  # 해당 좌표의 이전 방문 좌표를 저장
                queue.append(target)


n, k = map(int, input().split())
dist = [-1] * 100001  # 현재 좌표까지 이동한 시간을 저장할 리스트
visited = [-1] * 100001  # 이전 방문 좌표를 저장할 리스트

bfs()
