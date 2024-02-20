n = int(input())
target = int(input())
snail = [[0] * n for _ in range(n)]

# 6시, 3시, 12시, 9시 방향 순서
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

i, j = 0, 0
target_i, target_j = 0, 0  # target 숫자의 좌표
idx = 0  # 방향을 설정하기 위한 변수

# 0, 0 좌표부터 시작하여 n * n부터 0까지 내림차순으로 달팽이 만들기 진행
for number in range(n * n, 0, -1):
    snail[i][j] = number
    if number == target:  # 현재 숫자가 target이라면 좌표를 저장
        target_i, target_j = i + 1, j + 1

    ni, nj = i + di[idx % 4], j + dj[idx % 4]
    # 다음 이동좌표가 범위를 벗어나거나 숫자 저장이 되어있다면 방향 전환
    if (ni < 0 or ni >= n or nj < 0 or nj >= n) or snail[ni][nj]:
        idx += 1
        ni, nj = i + di[idx % 4], j + dj[idx % 4]
    i, j = ni, nj  # 다음 좌표 이월

# 달팽이 출력
for s in snail:
    print(*s)

print(target_i, target_j)  # target 숫자의 좌표 출력