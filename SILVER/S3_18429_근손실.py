def backtrack(idx, w, cnt, v):
    global ans

    # 모든 운동 플랜이 종료될 경우
    if cnt == n:
        # 최종 중량이 500 이상이라면 ans 1 추가
        if w >= 500:
            ans += 1
        return
    
    # 운동 중에 중량이 500 밑으로 떨어진다면 return
    if w < 500:
        return
    
    # 같은 인덱스나 방문 지역을 제외한 인덱스에 대해 방문 표시 후 백트래킹
    for i in range(n):
        if i == idx or visited[i]:
            continue

        v[i] = 1
        # 운동 플랜에 맞는 중량 증가와 k만큼 중량 감소
        backtrack(i, w + weight[i] - k, cnt + 1, v)
        v[i] = 0


n, k = map(int, input().split())
weight = list(map(int, input().split()))
visited = [0] * n
ans = 0  # 운동 플랜 내내 중량이 500 이상 유지될 수 있는 경우의 수

backtrack(-1, 500, 0, visited)

print(ans)
