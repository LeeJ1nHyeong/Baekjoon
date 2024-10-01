def search():
    # 단어 2개를 조합하여 팰린드롬인지 확인
    for i in range(n):
        word1 = words[i]
        for j in range(i + 1, n):
            word2 = words[j]

            # 두 단어의 순서를 바꾸면서 조합하여 팰린드롬 여부 확인
            p1 = word1 + word2

            if p1 == p1[::-1]:
                return p1

            p2 = word2 + word1

            if p2 == p2[::-1]:
                return p2

    return 0  # 팰린드롬이 되는 조합이 없다면 0 return


t = int(input())

for _ in range(t):
    n = int(input())
    words = [input() for _ in range(n)]

    print(search())
