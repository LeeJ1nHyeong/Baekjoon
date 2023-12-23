def calculator(value, lst, cnt): # 백트래킹 계산기
    global min_value, max_value

    if cnt == n:  # 계산이 모두 끝나면 최대값, 최소값 찾고 함수 종료
        min_value = min(min_value, value)
        max_value = max(max_value, value)
        return

    for i in range(4):
        if lst[i]:
            lst[i] -= 1
            if i == 0:
                value += numbers[cnt]
            elif i == 1:
                value -= numbers[cnt]
            elif i == 2:
                value *= numbers[cnt]
            elif i == 3:
                value /= numbers[cnt]

            value = int(value)
            
            # 다음 숫자 계산을 위한 백트래킹 진행
            calculator(value, lst, cnt + 1)
            
            # 백트래킹 후 이전 값으로 되돌리기
            lst[i] += 1
            if i == 0:
                value -= numbers[cnt]
            elif i == 1:
                value += numbers[cnt]
            elif i == 2:
                value /= numbers[cnt]
            elif i == 3:
                value *= numbers[cnt]

n = int(input())
numbers = list(map(int, input().split()))  # 숫자 리스트
operators = list(map(int, input().split()))  # 연산자 리스트

min_value, max_value = int(1e9), int(-1e9)

calculator(numbers[0], operators, 1)

print(max_value) # 최대값
print(min_value) # 최소값