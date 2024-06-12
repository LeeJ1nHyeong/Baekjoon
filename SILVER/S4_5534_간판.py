# 간판 사용 가능 여부 확인
def check(i):
    # 두번째 알파벳과 같은 인덱스 탐색
    for j in range(i + 1, len(old_sign)):
        if old_sign[j] == sign[1]:
            # 첫번째와 두번째 인덱스의 간격
            gap = j - i

            sign_idx = 2  # 새 간판 인덱스
            idx = j + gap  # 오래된 간판 인덱스

            # 일정한 간격으로 새 간판의 모든 알파벳이 순서대로 있는지 확인
            while idx < len(old_sign):
                # 원하는 알파벳이 나오지 않는다면 while문 종료
                if sign[sign_idx] != old_sign[idx]:
                    break

                # 새 간판 인덱스 1 증가, 오래된 간판 인덱스 gap만큼 증가
                sign_idx += 1
                idx += gap

                # 모든 알파벳이 있다면 True return
                if sign_idx == len(sign):
                    return True

    return False  # for문이 종료됐다면 조건이 맞지 않다는 뜻이므로 False return


n = int(input())

sign = input()

ans = 0  # 사용 가능한 간판 개수
for _ in range(n):
    old_sign = input()

    # 오래된 간판이 새 간판과 같은 이름이라면 ans 1 추가 후 continue
    if old_sign == sign:
        ans += 1
        continue

    # 새 간판의 첫번째 알파벳과 같은 인덱스 탐색
    for i in range(len(old_sign)):
        if old_sign[i] != sign[0]:
            continue

        # 조건이 맞다면 ans 1 추가
        if check(i):
            ans += 1
            break

print(ans)  # 사용 가능한 간판 개수 출력
