n = int(input())

# 집 위치를 오름차순으로 정렬
house = sorted(list(map(int, input().split())))

# 오름차순 정렬 후 중간값에 해당하는 값을 출력
# 집 개수가 짝수일 경우 중간값 두 개 중 더 작은 값을 출력
print(house[(n - 1) // 2])
