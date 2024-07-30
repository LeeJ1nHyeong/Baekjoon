n = int(input())
user = set()  # 유저 목록

cnt = 0  # 곰곰티콘 사용 횟수
for _ in range(n):
    log = input()
    # "ENTER"가 들어온다면 현재 유저 수 길이만큼 cnt에 추가 후 user 초기화
    if log == "ENTER":
        cnt += len(user)
        user.clear()

    # 유저 닉네임이 들어온다면 user에 추가
    else:
        user.add(log)

# 모든 기록 확인 후 user에 닉네임이 있을 경우 개수 만큼 cnt에 추가
if user:
    cnt += len(user)

# 곰곰티콘 사용 횟수 출력
print(cnt)
