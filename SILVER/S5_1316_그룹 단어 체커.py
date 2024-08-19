def check():
    alphabet = [word[0]]  # 단어의 첫 글자를 리스트에 추가한 상태로 시작

    for i in range(1, len(word)):
        # 이전 알파벳과 같은 알파벳이라면 continue
        if word[i] == word[i - 1]:
            continue

        # alphabet에 현재 알파벳이 있다면 False return
        if word[i] in alphabet:
            return False
        
        # alphabet에 현재 알파벳 추가
        alphabet.append(word[i])

    return True  # for문이 종료됐다면 조건을 만족한다는 뜻이므로 True return


n = int(input())

ans = 0  # 그룹 단어 개수
for _ in range(n):
    word = list(input())

    # 조건을 만족한다면 ans 1 추가
    if check():
        ans += 1

# 그룹 단어 개수 출력
print(ans)
