word = input()
new_word_list = []

# 단어를 각각 길이가 1 이상인 작은 단어 3개로 분리
for i in range(1, len(word)):
    word1 = word[:i]

    for j in range(i, len(word)):
        word2 = word[i:j]
        word3 = word[j:]

        # 길이가 0인 단어가 있다면 continue
        if not (len(word1) and len(word2) and len(word3)):
            continue

        # 각각의 단어들을 뒤집은 뒤 합친 상태로 new_word_list에 추가
        new_word = word1[::-1] + word2[::-1] + word3[::-1]
        new_word_list.append(new_word)

# 오름차순으로 정렬 후 사전 순으로 가장 위에 있는 단어 출력
new_word_list.sort()
print(new_word_list[0])
