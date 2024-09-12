n = int(input())
student_id = [input() for _ in range(n)]

ans = 1

while True:
    parse_id = set()

    # 각 학생 번호의 뒤에서 ans개의 자리수를 파싱하여 parse_id에 추가 
    for i in range(n):
        parse_id.add(student_id[i][-ans:])

    # parse_id의 길이가 n개라면(중복이 없다면) while문 종료
    if len(parse_id) == n:
        break

    # 중복이 있다면 계속 진행
    ans += 1

print(ans)
