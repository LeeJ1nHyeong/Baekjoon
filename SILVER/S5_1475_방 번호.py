n = input()
num_cnt = [0 for _ in range(9)]

for i in range(len(n)):
    target = int(n[i])
    if target == 6 or target == 9:  # 6, 9는 둘다 6번 인덱스에 1 추가
        num_cnt[6] += 1
    else:
        num_cnt[target] += 1

# 6번 인덱스 값을 2로 나누기
# 사사오입 원칙에 따라 round 사용이 안되기 때문에 경우의 수에 따라 6번 인덱스값 변형
if num_cnt[6] > 2 and num_cnt[6] % 2:
    num_cnt[6] = int(num_cnt[6] / 2) + 1
elif num_cnt[6] == 1:
    num_cnt[6] = 1
else:
    num_cnt[6] = int(num_cnt[6] / 2)

print(max(num_cnt))