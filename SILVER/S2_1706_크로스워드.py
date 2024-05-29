r, c = map(int, input().split())
puzzle = [list(input()) for _ in range(r)]
words = []  # 단어를 저장할 리스트

# 가로 탐색
for i in range(r):
    word = ""
    for j in range(c):
        # 금지 칸일 경우
        if puzzle[i][j] == "#":
            # 저장된 단어가 두 글자 이상이라면 words에 추가
            if len(word) >= 2:
                words.append(word)
            # 길이 여부 상관없이 단어 초기화
            word = ""
        # 영어일 경우 word에 글자 추가
        else:
            word += puzzle[i][j]

    # 탐색 후 단어가 두 글자 이상이라면 words에 추가
    if len(word) >= 2:
        words.append(word)

# 세로 탐색
for j in range(c):
    word = ""
    for i in range(r):
        # 금지 칸일 경우
        if puzzle[i][j] == "#":
            # 저장된 단어가 두 글자 이상이라면 words에 추가
            if len(word) >= 2:
                words.append(word)
            # 길이 여부 상관없이 단어 초기화
            word = ""
        # 영어일 경우 word에 글자 추가
        else:
            word += puzzle[i][j]

    # 탐색 후 단어가 두 글자 이상이라면 words에 추가
    if len(word) >= 2:
        words.append(word)

# 오름차순 정렬 후 첫번째 단어 출력
words.sort()
print(words[0])
