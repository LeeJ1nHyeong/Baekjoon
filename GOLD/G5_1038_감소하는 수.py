def backtrack(lst):  # 감소 수열을 찾기 위한 백트래킹
    for i in range(10):
        if not lst:  # 한 자리수일 경우에는 그냥 담기
            numbers.append([i])
            backtrack([i])
        else:  # 각 리스트의 마지막 원소가 i보다 크다면 i를 담은 뒤 numbers에 추가하고 백트래킹 진행
            if lst[-1] > i:
                numbers.append(lst + [i])
                backtrack(lst + [i])

n = int(input())
numbers = []  # 백트래킹으로 얻을 배열들을 모으는 리스트
num_list = []  # numbers에서 얻은 배열을 활용해서 int형으로 담을 리스트

backtrack([])  # 백트래킹 진행

# int형으로 전환하여 담기
for number in numbers:
    num = ''.join(map(str, number))
    if num == '0':
        num_list.append(0)
    else:
        num_list.append(int(num))

num_list.sort()  # 오름차순

if n > 1022:  # 최대 1022개가 나오기 때문에 n이 이 이상일 경우에는 -1 출력
    print(-1)
else:
    print(num_list[n])