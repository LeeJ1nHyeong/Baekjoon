import sys
input = sys.stdin.readline

n = int(input())

# 내림차순으로 정렬 후 하나씩 출력
number = sorted(list(int(input()) for _ in range(n)), reverse=True)

for num in number:
    print(num)
