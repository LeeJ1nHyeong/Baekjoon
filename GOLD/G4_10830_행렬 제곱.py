# 분할정복을 활용한 풀이

def divide(b, lst):  # 분할정복
    if b == 1:  # b == 1일 경우의 예외처리
        for i in range(n):
            for j in range(n):
                lst[i][j] %= 1000  # 문제 조건에 맞게 각 원소를 1000으로 나누기

        return lst

    divide_matrix = divide(b // 2, lst)  # 분할 진행

    # 짝수, 홀수에 따라 행렬 곱셈 진행
    if b % 2:
        return multiple(multiple(divide_matrix, divide_matrix), lst)
    else:
        return multiple(divide_matrix, divide_matrix)

def multiple(lst1, lst2):  # 행렬 곱셈

    multiple_matrix = [[0 for _ in range(n)] for _ in range(n)]  # 행렬 곱셈 결과값 저장용 리스트
    for i in range(n):
        for j in range(n):
            for k in range(n):
                multiple_matrix[i][j] += lst1[i][k] * lst2[k][j]  # 행렬 곱셈 진행

            multiple_matrix[i][j] %= 1000

    return multiple_matrix

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

ans = divide(b, matrix)

for a in ans:
    print(*a)