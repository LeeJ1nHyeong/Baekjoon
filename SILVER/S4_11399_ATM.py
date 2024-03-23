# 인출 시간의 최솟값은 대기시간을 오름차순하여 이전 값을 누적하여 더할 때 갖는다.

n = int(input())
wait = sorted(list(map(int, input().split())))

for i in range(1, n):
    wait[i] += wait[i - 1]  # 누적된 이전 값을 현재 값에 더하기

print(sum(wait))  # 대기시간 총 합을 출력