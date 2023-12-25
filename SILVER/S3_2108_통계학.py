import sys
input = sys.stdin.readline

n = int(input())

numbers = []  # 숫자를 담기 위한 리스트
numbers_dict = {}  # 최빈값을 구하기 위한 딕셔너리

for _ in range(n):
    number = int(input())
    numbers.append(number)
    if number in numbers_dict:
        numbers_dict[number] += 1
    else:
        numbers_dict[number] = 1

numbers.sort()  # 리스트 오름차순 정렬

max_numbers = max(numbers_dict.values())  # 최빈값
max_cnt_number = [i for i, j in numbers_dict.items() if max_numbers == j]  # 최빈값에 해당하는 숫자들을 리스트로 생성
max_cnt_number.sort()  # 오름차순 정렬

average = round(sum(numbers) / n)  # 산술평균
center = numbers[n // 2]  # 중간값
ranges = numbers[-1] - numbers[0]  # 범위

print(average)
print(center)
print(max_cnt_number[1] if len(max_cnt_number) > 1 else max_cnt_number[0])
print(ranges)