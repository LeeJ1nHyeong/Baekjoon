from collections import deque


def bfs():
    s, t = map(int, input().split())
    queue = deque([(s, t, 0)])  # 초기 점수와 발차기 횟수를 튜플 형태로 queue에 저장

    while queue:
        cs, ct, cnt = queue.popleft()
        if cs == ct:  # 두 점수가 같다면 발차기 횟수 return
            return cnt
        
        # A 발차기 후 s가 t보다 점수가 같거나 작다면 해당 점수를 queue에 추가
        if cs * 2 <= ct + 3:
            queue.append((cs * 2, ct + 3, cnt + 1))
        # B 발차기 후의 점수도 queue에 추가
        queue.append((cs + 1, ct, cnt + 1))


c = int(input())

for _ in range(c):
    print(bfs())
