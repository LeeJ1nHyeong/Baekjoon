word = input()
suffix = []  # 접미사를 담을 리스트

# 앞의 알파벳을 없애면서 suffix에 단어 추가
for i in range(len(word)):
    suffix.append(word[i:])

# 오름차순 정렬 후 순서대로 출력
suffix.sort()
for s in suffix:
    print(s)
