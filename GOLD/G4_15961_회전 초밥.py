# 슬라이딩 윈도우를 이용한 풀이

n, d, k, c = map(int, input().split())

sushi_belt = []  # 벨트에 있는 회전초밥을 담을 리스트
sushi_list = [0 for _ in range(d + 1)]  # 해당 번호의 초밥을 먹었는지 확인을 위한 리스트

for _ in range(n):
    num = int(input())
    sushi_belt.append(num)

cnt = 0

# 처음 K개의 초밥 탐색
for i in range(k):
    if not sushi_list[sushi_belt[i]]:
        cnt += 1
    sushi_list[sushi_belt[i]] += 1

max_cnt = cnt

# 슬라이딩 윈도우
for i in range(n):
    # 쿠폰 번호의 초밥을 먹었는지 확인
    if max_cnt <= cnt:
        if not sushi_list[c]:
            max_cnt = cnt + 1
        else:
            max_cnt = cnt

    if max_cnt == k + 1:  # 이론상 최대값은 k+1이기 때문에 예외처리
        break

    # 가장 왼쪽의 초밥을 제외
    sushi_list[sushi_belt[i]] -= 1
    if not sushi_list[sushi_belt[i]]:  # 윈도우 내에 같은 번호가 있는지 확인
        cnt -= 1

    # 다음 초밥 추가
    if not sushi_list[sushi_belt[(k + i) % n]]:  # 윈도우 내에 같은 번호가 있는지 확인
        cnt += 1
    sushi_list[sushi_belt[(k + i) % n]] += 1

print(max_cnt)