def search(target, opposite):
    global ans

    color = 0  # 연속된 색깔의 개수

    cnt = 0  # 옮길 횟수

    for i in range(n):
        # 탐색 색깔일 경우 color 1 추가
        if ball[i] == target:
            color += 1

        # 반대 색깔이고 color에 값이 있다면 cnt에 color를 더하고 color 초기화
        if ball[i] == opposite and color:
            cnt += color
            color = 0

    # 탐색 종료 후 cnt를 ans에 추가
    ans.append(cnt)


n = int(input())
ball = input()
ans = []

# 정방향으로 색깔별 탐색
search("R", "B")
search("B", "R")

# ball 순서를 뒤집고 색깔별 탐색
ball = ball[::-1]
search("R", "B")
search("B", "R")

# ans내에 있는 값 중 최솟값 출력
print(min(ans))
