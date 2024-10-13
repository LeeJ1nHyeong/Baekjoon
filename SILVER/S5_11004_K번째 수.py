n, k = map(int, input().split())

# 오름차순 정렬로 입력
num_list = sorted(list(map(int, input().split())))

# k번째 수 ((k - 1)번째 인덱스) 출력
print(num_list[k - 1])
