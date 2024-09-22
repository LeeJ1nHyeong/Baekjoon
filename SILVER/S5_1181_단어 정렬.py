n = int(input())
words = list({input() for _ in range(n)})

# 단어 길이 오름차순, 길이가 같다면 사전 순으로 정렬 후 출력
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
