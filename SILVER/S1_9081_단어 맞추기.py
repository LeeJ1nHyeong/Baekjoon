t = int(input())


def find_next(word):
    # 단어의 마지막부터 탐색하여 현재의 알파벳이 이전의 알파벳보다 뒷 순위일 경우를 찾기
    for i in range(len(word) - 1, 0, -1):
        if word[i - 1] < word[i]:
            # 다시 마지막부터 해당 인덱스까지 탐색 진행
            for j in range(len(word) - 1, i - 1, -1):
                # j의 순서가 i - 1보다 클 경우 두 알파벳 순서를 교환
                if word[i - 1] < word[j]:
                    word[i - 1], word[j] = word[j], word[i - 1]
                    # (처음 ~ i - 1번째 단어) + (i부터 끝까지의 단어를 뒤집은 결과)를 합쳐서 return
                    return word[:i] + word[i:][::-1]

    return word  # 사전 순서상 마지막 단어라면 그대로 return


for _ in range(t):
    word = list(input())
    print("".join(find_next(word)))
