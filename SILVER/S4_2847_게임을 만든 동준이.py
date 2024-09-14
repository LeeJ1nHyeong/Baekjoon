n = int(input())
score = [int(input()) for _ in range(n)]

cnt = 0  # 점수 변경 횟수

# 마지막 레벨 점수부터 거꾸로 탐색
for i in range(n - 1, 0, -1):
    # 현재 레벨 점수가 이전 레벨 점수보다 낮다면
    if score[i] <= score[i - 1]:
        # 두 점수 차이에 1을 더한 값을 cnt에 추가
        cnt += score[i - 1] - score[i] + 1

        # 이전 레벨 점수에도 같은 값만큼 차감
        score[i - 1] -= score[i - 1] - score[i] + 1

# 점수 변경 횟수 출력
print(cnt)
