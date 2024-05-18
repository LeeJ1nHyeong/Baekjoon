# 백트래킹
def backtrack(idx, lst):
    global min_diff

    # 팀 분배가 완료됐을 경우 능력치 차이의 최솟값 여부 확인
    if sum(lst) == n // 2:
        min_diff = min(min_diff, check(lst))
        return
    
    # 팀원 분배 진행
    for i in range(idx, n):
        lst[i] = 1
        backtrack(i + 1, lst)
        lst[i] = 0

# 능력치 비교
def check(lst):
    team_start, team_link = 0, 0  # 스타트 팀, 링크 팀 능력치

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            # 같은 팀에 소속된 두 사람 간의 능력치를 각 팀에 더하기
            if lst[i] and lst[j]:
                team_start += ability[i][j]
            elif not lst[i] and not lst[j]:
                team_link += ability[i][j]

    return abs(team_start - team_link)  # 두 팀간의 능력치 차이 return


n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
min_diff = 100 * n  # 능력치 차이 최솟값

team = [0] * n  # 같은 팀 여부를 확인할 리스트, 1은 스타트 팀, 0은 링크 팀

backtrack(0, team)  # 백트래킹 진행

print(min_diff)  # 능력치 차이 최솟값 출력
