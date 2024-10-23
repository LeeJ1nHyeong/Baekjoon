import math

t = int(input())

# 경우의 수는 mCn= m! / ((m - n)! *  n!)
for _ in range(t):
    n, m = map(int, input().split())
    ans = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(ans)