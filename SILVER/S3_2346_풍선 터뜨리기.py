from collections import deque

n = int(input())
move = list(map(int, input().split()))
balloon = deque()  # 풍선 덱
ans = []  # 풍선 터뜨리는 순서

# 풍선 번호와 다음 이동 값을 튜플 형태로 덱에 저장
for i in range(n):
    balloon.append((i + 1, move[i]))

# 회전 형태의 덱으로 생각하면서 탐색 진행
while balloon:
    num, m = balloon.popleft()
    # 풍선 번호를 ans에 저장
    ans.append(num)

    # 이동 방향이 양수일 경우 반시계방향 회전
    if m > 0:
        balloon.rotate(-(m - 1))
    # 이동 방향이 음수일 경우 시계방향 회전
    else:
        balloon.rotate(-m)

# 풍선 터뜨리는 순서 출력
print(*ans)
