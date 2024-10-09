t = int(input())

for _ in range(t):
    n, *student = map(int, input().split())

    line = []  # 줄 세우기
    ans = 0  # 학생 이동 횟수 합
    for i in range(20):
        now = student[i]

        # 새로 세운 줄을 탐색하여 현재 학생의 키보다 큰 학생이 있다면 해당 학생을 포함하여 뒤에 있는 학생 수를 ans에 더함
        for j in range(len(line)):
            if student[i] < line[j]:
                ans += len(line) - j
                break

        # 현재 학생의 키를 line에 포함 후 오름차순 정렬
        line.append(student[i])
        line.sort()

    print(n, ans)
