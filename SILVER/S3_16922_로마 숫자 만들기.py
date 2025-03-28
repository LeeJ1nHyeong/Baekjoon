def backtrack(cnt, idx):
    global number

    if cnt == n:
        numbers.add(number)
        return

    for i in range(idx, 4):
        number += roma[i]
        backtrack(cnt + 1, i)
        number -= roma[i]


n = int(input())
roma = [1, 5, 10, 50]
numbers = set()
number = 0

backtrack(0, 0)
print(len(numbers))
