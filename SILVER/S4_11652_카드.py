import sys
input = sys.stdin.readline

n = int(input())
number = {}

# 해시에 숫자 추가
for _ in range(n):
    num = int(input())

    # 해시에 숫자가 없다면 새로 추가, 있다면 해당 숫자의 value값 1 추가 
    if num not in number:
        number[num] = 1
    else:
        number[num] += 1

# 해시 내의 key들을 리스트화. value 내림차순, value가 같다면 key 오름차순으로 정렬
num_list = sorted(number.keys(), key=lambda x: (-number[x], x))

# 가장 많이 갖고 있는 정수 출력
print(num_list[0])
