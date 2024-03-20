document = input()
word = input()

d, w = len(document), len(word)  # 문서 길이, 단어 길이

idx = 0  # 시작 인덱스
cnt = 0  # 중복 없이 나오는 단어 개수

while idx <= d - w:
    # idx에서 시작한 단어가 word라면 cnt 1 추가 및 idx에 w 추가
    if document[idx : idx + w] == word:
        cnt += 1
        idx += w

    # word가 아니라면 다음 idx로 진행
    else:
        idx += 1

print(cnt)