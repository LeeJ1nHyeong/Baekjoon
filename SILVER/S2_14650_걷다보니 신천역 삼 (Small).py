def backtrack(cnt, number):
    if cnt == n:
        if int(number) % 3 == 0:
            numbers.add(int(number))
        return

    for i in ["0", "1", "2"]:
        if cnt == 0 and i == "0":
            continue

        backtrack(cnt + 1, number + i)


n = int(input())
numbers = set()

backtrack(0, "")
print(len(numbers))
