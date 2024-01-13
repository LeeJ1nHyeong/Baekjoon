n, x = map(int, input().split())
visitor = [0] + list(map(int, input().split()))

max_visitor = 0
cnt = 0

for i in range(1, x + 1):  # 1일차 부터 x일차 까지의 블로그 방문자 확인
    max_visitor += visitor[i]

if max_visitor:  # 0이 아니라면 cnt 1부터 시작
    cnt += 1

visitor_cnt = max_visitor

# 슬라이딩 윈도우
for i in range(1, n - x + 1):
    visitor_cnt -= visitor[i]  # 가장 왼쪽 값을 제외
    visitor_cnt += visitor[x + i]  # 다음 값 추가

    if max_visitor == visitor_cnt:  # 현재 최댓값과 같다면 cnt 1 추가
        cnt += 1
    elif max_visitor < visitor_cnt:  # 현재 최댓값보다 크다면 그 값을 최댓값으로 저장 후 cnt 1로 초기화
        max_visitor = visitor_cnt
        cnt = 1

if max_visitor == 0:  # 최댓값이 0일 경우의 예외처리
    print("SAD")
else:
    print(max_visitor)
    print(cnt)