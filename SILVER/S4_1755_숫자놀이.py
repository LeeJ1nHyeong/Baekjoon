m, n = map(int, input().split())
dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

numbers = []

for i in range(m, n + 1):
    word = " ".join([dict[j] for j in str(i)])
    numbers.append((word, i))

numbers.sort(key=lambda x: x[0])

# 한 줄당 10개 단위로 출력
for i in range(len(numbers)):
    if i % 10 == 0 and i != 0:
        print()
    print(numbers[i][1], end=" ")
