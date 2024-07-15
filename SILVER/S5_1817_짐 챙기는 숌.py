n, m = map(int, input().split())
# n이 0일 경우 예외처리
if not n:
    print(0)

else:
    book = list(map(int, input().split()))

    weight = 0  # 박스에 담을 책 무게
    cnt = 1  # 책이 1개 이상일 경우 박스 1개는 무조건 필요

    for i in range(n):
        # 박스에 담긴 책 무게와 현재 책의 무게 합이 박스 최대 무게보다 클 경우 박스 개수 1 추가 후 weight를 현재 책 무게로 저장
        if weight + book[i] > m:
            cnt += 1
            weight = book[i]
        # 위 조건이 아닐 경우 weight에 현재 책 무게 추가
        else:
            weight += book[i]

    # 필요한 최소 박스 개수 출력
    print(cnt)
    