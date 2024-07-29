n = int(input())
study = []  # 공부 기록
baekjoon = []  # 백준 기록

for _ in range(n):
    record = input()

    # 백준 기록일 경우 숫자만 파싱하여 baekjoon에 int로 저장
    if "boj.kr/" in record:
        baekjoon.append(int(record[7:]))
    # 공부 기록일 경우 study에 저장
    else:
        study.append(record)

# study는 문자열 길이 오름차순, 같다면 아스키코드 오름차순으로 정렬
study.sort(key=lambda x: (len(x), x))
# 백준은 문제 번호 오름차순으로 정렬
baekjoon.sort()

# 공부 기록 먼저 출력 후 백준 문제 기록 출력
for s in study:
    print(s)
for b in baekjoon:
    print(f"boj.kr/{b}")
