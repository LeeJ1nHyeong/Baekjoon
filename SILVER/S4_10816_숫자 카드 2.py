import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

seek = [0 for _ in range(M)]

N_dict = {}  # 숫자 개수를 저장하기 위해 딕셔너리 사용

while N_list:
    N_num = N_list.pop()
    # pop으로 나온 숫자가 딕셔너리에 key로 존재하면 해당 key의 value 1 추가
    if N_num in N_dict:
        N_dict[N_num] += 1
    # 없다면 key를 새로 생성
    else:
        N_dict[N_num] = 1

for i in range(M):
    # 숫자 카드가 딕셔너리 내 키에 존재하면 인덱스에 해당하는 seek에 값 반영
    if M_list[i] in N_dict.keys():
        seek[i] = N_dict[M_list[i]]

print(*seek)