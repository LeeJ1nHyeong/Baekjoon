from collections import deque

t = int(input())

for _ in range(t):
    # 울음소리들을 덱에 저장
    sounds = deque(list(map(str, input().split())))

    while True:
        sentence = input()
        # "what does the fox say?" 문장이 나오면 덱에 저장된 울음소리들을 출력 후 while문 종료
        if sentence == "what does the fox say?":
            print(*sounds)
            break

        # "<동물> goes <울음소리>" 형태의 문장이 나오면 울음소리를 파싱
        sound = list(sentence.split())[2]

        # 덱에 저장된 해당 울음소리를 모두 제거
        while sound in sounds:
            sounds.remove(sound)
