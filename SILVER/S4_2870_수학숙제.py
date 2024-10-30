n = int(input())
num_list = []

for _ in range(n):
    word = input()
    num = ""

    # 숫자 여부 탐색
    for w in word:
        # 숫자라면 num에 문자열 추가
        if w.isdigit():
            num += w
        else:
            # 숫자가 아니라면 num을 int형으로 num_list에 추가 후 초기화
            if num:
                num_list.append(int(num))
                num = ""

    # 단어 탐색 종료 후 num에 숫자가 남아있다면 num_list에 추가
    if num:
        num_list.append(int(num))

# 파싱한 숫자들을 오름차순으로 정렬 후 순서대로 출력
num_list.sort()

for nl in num_list:
    print(nl)
