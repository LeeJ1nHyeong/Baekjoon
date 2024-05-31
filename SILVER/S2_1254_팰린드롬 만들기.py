word = input()

# 처음 단어가 팰린드롬이라면 단어의 길이 그대로 출력
if word == word[::-1]:
    print(len(word))

else:
    # 1번 인덱스부터 시작되는 단어가 팰린드롬일 경우 처음 단어 길이에서 인덱스를 더한 값을 출력
    for i in range(1, len(word)):
        if word[i:] == word[:i - 1:-1]:
            print(len(word) + i)
            break
