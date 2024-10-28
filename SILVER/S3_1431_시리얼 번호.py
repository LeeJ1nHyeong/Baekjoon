def num_total(x):
    total = 0

    # 단어 내의 숫자 합 구하기
    for i in range(len(x)):
        if x[i].isdigit():
            total += int(x[i])

    return total  # 숫자 합 출력


n = int(input())
word = [input() for _ in range(n)]

# 단어 길이, 단어 내 숫자의 합, 사전 순서대로 정렬
word.sort(key=lambda x: (len(x), num_total(x), x))

for w in word:
    print(w)
