import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
ans = 0  # 경우의 수 개수
a.sort()  # 이분 탐색을 위한 오름차순 정렬

for i in range(n - 1):
    # 현재 인덱스의 다음 인덱스와 가장 마지막 인덱스를 투 포인터로 시작
    left, right = i + 1, n - 1
    max_idx = n  # 중복 개수를 체크하기 위한 인덱스

    while left != right:
        # 세 숫자의 합이 0일 경우
        if a[i] + a[left] + a[right] == 0:
            # 두 포인터의 숫자가 같다면 두 포인터의 간격 값을 ans에 더해줌
            if a[left] == a[right]:
                ans += right - left
            # 두 포인터의 숫자가 다를 경우
            else:
                # 오른쪽 포인터 값의 중복 개수 체크
                if max_idx > right:
                    max_idx = right
                    while max_idx >= 0 and a[max_idx - 1] == a[right]:
                        max_idx -= 1
                # 중복 개수를 반영한 값을 ans에 더해주고
                ans += right - max_idx + 1
            left += 1  # 왼쪽 포인터를 오른쪽으로 1칸 이동

        # 세 숫자의 합이 0보다 클 경우 오른쪽 포인터를 왼쪽으로 1칸 이동
        elif a[i] + a[left] + a[right] > 0:
            right -= 1

        # 세 숫자의 합이 0보다 작을 경우 왼쪽 포인터를 오른쪽으로 1칸 이동
        elif a[i] + a[left] + a[right] < 0:
            left += 1

print(ans)  # 경우의 수 출력