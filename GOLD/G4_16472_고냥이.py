n = int(input())
word = list(input())
dict = {}

left, right = 0, 0
ans = 0

while left < len(word) and right < len(word):
    if word[right] not in dict:
        dict[word[right]] = 1
    else:
        dict[word[right]] += 1

    if len(dict) > n:
        while left <= right and len(dict) > n:
            dict[word[left]] -= 1
            if dict[word[left]] == 0:
                del dict[word[left]]

            left += 1

    ans = max(ans, right - left + 1)

    right += 1

print(ans)
