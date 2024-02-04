# 비트마스킹을 이용한 풀이

n = int(input())
subjects = []  # 과목 시간표를 담을 리스트

# 과목 시간표 리스트 담기
for _ in range(n):
    k, *t = map(int, input().split())
    subjects.append(t)

m = int(input())
for _ in range(m):
    p, *q = map(int, input().split())
    q_bit = 0  # 학생의 비어있는 시간표를 이진수 형태로 담을 변수
    for i in range(p):
        q_bit += 2 ** q[i]  # 각 학생의 시간표을 이진수 형태로 담음

    ans = 0

    for subject in subjects:
        cnt = 0
        # 과목의 시간표가 q_bit에 담겨져 있는지 확인
        for i in range(len(subject)):
            # 0이 아니라면 해당 비트에 값이 담겨져있다는 뜻이므로 cnt 1 추가
            if q_bit & (1 << subject[i]):
                cnt += 1

        if cnt == len(subject):  # 과목 시간표가 모두 담겨저 있다면 ans 1 추가
            ans += 1

    print(ans)