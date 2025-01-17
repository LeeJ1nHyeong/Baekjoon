word = input()
new_words = []

for i in range(len(word) - 2):
    for j in range(i + 1, len(word) - 1):
        part1, part2, part3 = word[:i + 1], word[i + 1:j + 1], word[j + 1:]
        new_word = part1[::-1] + part2[::-1] + part3[::-1]

        new_words.append(new_word)

new_words.sort()
print(new_words[0])
