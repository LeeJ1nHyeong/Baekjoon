import sys
input = sys.stdin.readline

n = int(input())
fruit = list(map(int, input().split()))

cnt_fruit = [0] * 10  # 총 과일 개수
tanghuru_fruit = [0] * 10  # 탕후루 과일 종류 개수

# 첫 과일을 개수에 추가
cnt_fruit[fruit[0]] += 1
tanghuru_fruit[fruit[0]] = 1

ans = 1  # 두 종류 이하 과일 탕후루의 최대 길이
l, r = 0, 0  # 투 포인터

while True:
    # 과일 종류가 2개 이하일 경우
    if sum(tanghuru_fruit) <= 2:
        # 최대 길이 여부 확인
        ans = max(ans, sum(cnt_fruit))

        # 오른쪽 포인터 1 추가
        r += 1

        # 오른쪽 포인터가 n이 된다면 while문 종료
        if r == n:
            break

        # 오른쪽 포인터의 과일 개수 추가
        cnt_fruit[fruit[r]] += 1
        tanghuru_fruit[fruit[r]] = 1

    # 과일 종류가 3개 이상일 경우
    else:
        # 왼쪽 포인터의 과일 개수 추가
        cnt_fruit[fruit[l]] -= 1

        # 왼쪽 포인터 과일이 없어진다면 과일 종류에서 제외
        if not cnt_fruit[fruit[l]]:
            tanghuru_fruit[fruit[l]] = 0

        # 왼쪽 포인터 1 추가
        l += 1

# 최대 길이 출력
print(ans)
