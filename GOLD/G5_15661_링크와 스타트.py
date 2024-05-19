# 백트래킹
def backtrack(idx, team, cnt):
    global min_diff

    if cnt > n // 2:  # 팀원 분배 인원이 절반을 넘길 경우 return
        return
    
    # 팀원이 한 명 이상일 경우 능력치 차이 최솟값 여부 확인
    if cnt >= 1:
        min_diff = min(min_diff, check(team))

    # 팀원 분배를 비트마스킹 형태로 저장하여 백트래킹 진행
    for i in range(idx, n):
        backtrack(i + 1, team + 2 ** i, cnt + 1)

# 능력치 비교
def check(bit):
    team_start, team_link = 0, 0  # 스타트 팀, 링크 팀 능력치
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            # 비트마스킹으로 저장된 팀원 목록에 두 팀원이 같이 있을 경우 스타트 팀에 능력치를 더하기
            if (bit & 1 << i) and (bit & 1 << j):
                team_start += ability[i][j]
            # 두 팀원이 같이 없을 경우 링크 팀에 능력치를 더하기
            elif not (bit & 1 << i) and not (bit & 1 << j):
                team_link += ability[i][j]

    return abs(team_start - team_link)  # 두 팀간의 능력치 차이 return


n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
min_diff = 100 * n  # 두 팀간 능력치 차이 최솟값

backtrack(0, 0, 0)  # 백트래킹 진행

print(min_diff)  # 능력치 차이 최솟값 출력
