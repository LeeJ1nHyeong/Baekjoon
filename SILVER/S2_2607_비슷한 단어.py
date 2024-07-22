n = int(input())
first_word = list(input())  # 첫번째 단어
ans = 0  # 첫번째 단어와 비슷한 단어 개수

# 이 후의 단어를 첫번째 단어와 비교
for _ in range(n - 1):
    target = first_word[:]
    word = input()

    cnt = 0
    for w in word:
        # 비교 단어의 알파벳이 첫번째 단어에 있다면 첫번째 단어에서 알파벳 제거
        if w in target:
            target.remove(w)
        # 없다면 cnt 1 추가
        else:
            cnt += 1

    # 비교 후 첫번째 단어의 길이가 1 이하이면서 cnt가 1 이하라면 비슷한 단어이므로 ans 1 추가
    if len(target) <= 1 and cnt <= 1:
        ans += 1

# 비슷한 단어 개수 출력
print(ans)
