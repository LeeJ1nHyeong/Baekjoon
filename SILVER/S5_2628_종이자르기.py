r, c = map(int, input().split())
n = int(input())
row_list = [0, c]  # 가로 길이
column_list = [0, r]  # 세로 길이

# 가로, 세로 별로 자를 위치를 해당 리스트에 추가
for _ in range(n):
    d, line = map(int, input().split())
    if d == 0:
        row_list.append(line)
    else:
        column_list.append(line)

# 오름 차순 정렬
row_list.sort()
column_list.sort()

max_row, max_column = 0, 0  # 가로, 세로 최대 길이

# 자를 위치와 이전 위치의 차이를 계산 후 최댓값 여부 확인
for i in range(1, len(row_list)):
    row = row_list[i] - row_list[i - 1]
    max_row = max(row, max_row)

for i in range(1, len(column_list)):
    column = column_list[i] - column_list[i - 1]
    max_column = max(column, max_column)

# 가로 최댓값, 세로 최댓값을 곱한 값을 출력
ans = max_row * max_column
print(ans)
