# 시계수 찾기
def clock_number(lst):
    min_num = 9999
    # 숫자 4가지를 시계방향 순서대로 조합하여 최솟값을 return
    for i in range(4):
        num = "".join(lst[i:] + lst[:i])
        min_num = min(int(num), min_num)
    return min_num


number = list(input().split())
cn = clock_number(number)  # 시계수 탐색

ans = 1
# 1111부터 시계수까지 수를 탐색하여 몇 번째로 작은 수인지 탐색
for i in range(1111, cn):
    if "0" not in str(i) and clock_number(list(str(i))) == i:
        ans += 1

# 시계수 순위 출력
print(ans)
