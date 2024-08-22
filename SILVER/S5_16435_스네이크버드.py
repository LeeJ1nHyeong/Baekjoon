n, l = map(int, input().split())
# 과일 높이를 오름차순으로 정렬한 상태로 저장
fruit = sorted(list(map(int, input().split())))

# 스네이크버드의 길이가 과일 높이보다 낮다면 break
for i in range(n):
    if l < fruit[i]:
        break

    # 길이가 높이보다 길거나 같다면 길이 1 증가
    l += 1

# 스네이크버드의 길이 출력
print(l)
