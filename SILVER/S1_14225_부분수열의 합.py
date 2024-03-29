# dfs (내 풀이)
def dfs(idx, total):
    # 현재 부분 수열 합이 미방문이라면 방문 체크
    if not visited[total]:
        visited[total] = 1
    
    # 인덱스 중복이 되지 않게 dfs 진행
    for i in range(idx + 1, n):
        dfs(i, total + s[i])


n = int(input())
s = list(map(int, input().split()))

# 나올 수 있는 최댓값인 n * 100000 까지의 방문 체크용 1차원 리스트 생성
visited = [0] * (n * 100000 + 1)

# 부분 수열 합을 dfs 방식으로 탐색
for i in range(n):
    dfs(i, s[i])

# 방문 체크가 되지 않은 첫 숫자를 출력 후 for문 종료
for i in range(1, n * 100000 + 1):
    if not visited[i]:
        print(i)
        break


# 그리디
n = int(input())
s = list(map(int, input().split()))

s.sort()  # 오름차순 정렬

ans = 0  # 이전 값들의 합
for i in range(n):
    # ans + 1 이 현재 값보다 작다면 현재 조합으로 만들 수 없는 가장 작은 자연수이므로 for문 종료
    if ans + 1 < s[i]:
        break
    ans += s[i]  # 그렇지 않다면 현재 값을 더하기

print(ans + 1)