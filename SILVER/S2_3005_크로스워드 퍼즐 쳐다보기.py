r, c = map(int, input().split())
puzzle = [list(input()) for _ in range(r)]
words = []  # 단어 저장 리스트

# 가로 탐색
for i in range(r):
    word = ""
    for j in range(c):
        # "#"이 나올 경우 단어가 2글자 이상이면 words에 추가
        if puzzle[i][j] == "#":
            if len(word) >= 2:
                words.append(word)
            # 추가 여부 상관없이 단어 초기화
            word = ""
        # 알파벳일 경우 word에 추가
        else:
            word += puzzle[i][j]

    # 각 가로줄 탐색 후 단어가 2글자 이상이라면 words에 추가
    if len(word) >= 2:
        words.append(word)

# 세로도 가로와 동일한 방법으로 탐색
for j in range(c):
    word = ""
    for i in range(r):
        if puzzle[i][j] == "#":
            if len(word) >= 2:
                words.append(word)
            word = ""
        else:
            word += puzzle[i][j]

    if len(word) >= 2:
        words.append(word)

# 오름차순 정렬 후 첫 번째 단어 출력
words.sort()
print(words[0])