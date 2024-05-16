n = int(input())
friend = [list(input()) for _ in range(n)]

two_friend = [[0] * n for _ in range(n)]  # 2-친구 여부를 저장할 2차원 리스트

# i와 j가 2-친구 관계인지 탐색
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # 두 사람이 친구 관계거나 두 사람 모두 k의 친구 관계일 경우 2-친구 관계 성립
            if friend[i][j] == "Y" or (friend[i][k] == "Y" and friend[k][j] == "Y"):
                two_friend[i][j] = 1

# 가장 유명한 사람의 2-친구 수 출력
ans = 0
for tf in two_friend:
    ans = max(ans, sum(tf))
print(ans)
