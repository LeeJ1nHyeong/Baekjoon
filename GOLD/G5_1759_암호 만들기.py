def backtrack(idx, word, aeiou_cnt):  # 인덱스, 단어, 모음 개수
    # 단어 길이가 l일 경우 모음과 자음 개수 조건 충족이 된다면 출력 후 return
    if len(word) == l:
        if aeiou_cnt >= 1 and l - aeiou_cnt >= 2:
            print(word)
        return
    
    # 모음일 경우 모음 개수를 1 증가한 상태로 백트래킹
    for i in range(idx, c):
        if alphabet[i] in aeiou:
            backtrack(i + 1, word + alphabet[i], aeiou_cnt + 1)
        else:
            backtrack(i + 1, word + alphabet[i], aeiou_cnt)


l, c = map(int, input().split())

alphabet = list(map(str, input().split()))
alphabet.sort()  # 알파벳 오름차순 정렬
aeiou = ["a", "e", "i", "o", "u"]  # 모음

backtrack(0, "", 0)  # 백트래킹 진행
