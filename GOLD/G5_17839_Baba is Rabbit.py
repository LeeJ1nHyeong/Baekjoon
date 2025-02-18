from collections import deque

n = int(input())
objects = {}

for _ in range(n):
    p, q = input().split(" is ")

    # p를 key로 갖는 값들을 리스트로 저장
    if p not in objects:
        objects[p] = [q]
    else:
        objects[p].append(q)

ans = {}  # 방문 표시용
queue = deque(["Baba"])  # "Baba"부터 탐색 시작

while queue:
    now = queue.popleft()

    if now not in objects:
        continue

    for o in objects[now]:
        if o not in ans:
            ans[o] = 1
            queue.append(o)

ans = sorted(ans.keys())
for a in ans:
    print(a)
