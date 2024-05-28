'''
피보나치 수 점화식을 만들 경우 [[1, 1], [1, 0]] 행렬을 제곱하는 형태의 행렬식이 나온다.
'''

# 행렬 곱셈
def multiple(m1, m2):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += m1[i][k] * m2[k][j] % 1000000007

    return temp

# 분할정복
def power(matrix, n):
    if n == 1:
        return matrix
    
    # 분할정복을 활용하여 행렬 제곱 진행
    else:
        m = power(matrix, n // 2)
        if n % 2 == 0:
            return multiple(m, m)
        else:
            return multiple(multiple(m, m), matrix)


n = int(input())
dp = [[1, 1], [1, 0]]  # 제곱을 진행할 행렬
ans = power(dp, n)
print(ans[0][1] % 1000000007)  # 조건에 맞게 출력
