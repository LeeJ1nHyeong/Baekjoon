# 모음
vowel = ["a", "i", "y", "e", "o", "u"]
# 자음
consonant = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]

# 여러 문장이 입력으로 들어오기 때문에 try-except문 사용
while True:
    try:
        sentence = list(input())

        for i in range(len(sentence)):
            # 알파벳이 아닐 경우 continue
            if not sentence[i].isalpha():
                continue

            # 대문자일 경우
            if sentence[i].isupper():
                # 모음일 경우
                if sentence[i].lower() in vowel:
                    idx = vowel.index(sentence[i].lower())
                    sentence[i] = vowel[(idx + 3) % 6].upper()

                # 자음일 경우
                else:
                    idx = consonant.index(sentence[i].lower())
                    sentence[i] = consonant[(idx + 10) % 20].upper()

            # 소문자일 경우
            else:
                # 모음일 경우
                if sentence[i] in vowel:
                    idx = vowel.index(sentence[i])
                    sentence[i] = vowel[(idx + 3) % 6]

                # 자음일 경우
                else:
                    idx = consonant.index(sentence[i])
                    sentence[i] = consonant[(idx + 10) % 20]
        
        # 변환한 문장을 형식에 맞게 출력
        print("".join(sentence))

    except:
        break
