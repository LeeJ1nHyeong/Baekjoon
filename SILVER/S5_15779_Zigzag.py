n = int(input())
numbers = list(map(int, input().split()))

max_length = 2
length = 2

for i in range(n - 2):
    # 연속된 3개의 수가 오름차순이거나 내림차순이라면 length를 2로 초기화
    if numbers[i] <= numbers[i + 1] <= numbers[i + 2] or numbers[i] >= numbers[i + 1] >= numbers[i + 2]:
        length = 2
    # 지그재그 수열이라면 length 1 추가
    else:
        length += 1

    max_length = max(length, max_length)

print(max_length)
