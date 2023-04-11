def backtrack(i):
    global cnt
    if i == N:
        cnt += 1
        return

    else:
        for j in range(N):
            chess[i] = j
            if check(i):
                backtrack(i + 1)

def check(i):
    for k in range(i):
        if chess[i] == chess[k] or abs(chess[i] - chess[k]) == i - k:
            return False
    return True

N = int(input())
cnt = 0

chess = [0] * N

backtrack(0)

print(cnt)