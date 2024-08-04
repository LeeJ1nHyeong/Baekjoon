t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    box = []

    # 상자의 크기(가로 * 세로)를 box에 추기
    for _ in range(n):
        r, c = map(int, input().split())
        box.append(r * c)

    # 상자 크기 내림차순으로 정렬
    box.sort(reverse=True)

    ans = 0  # 필요한 상자 최소 개수
    candy = 0  # 담은 사탕 개수

    # 크기가 큰 상자부터 순서대로 탐색
    for i in range(n):
        ans += 1
        candy += box[i]
        # 담은 사탕 수가 할당된 사탕 수보다 크거나 같다면 탐색 종료
        if candy >= j:
            break

    # 필요한 상자 최소 개수 출력
    print(ans)
