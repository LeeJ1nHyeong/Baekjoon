n = int(input())
words = []

for _ in range(n):
    word = input()

    check = False
    for i in range(len(word)):
        new_word = word[i:] + word[:i]
        if new_word in words:
            check = True
            break

    if not check:
        words.append(word)

print(len(words))
