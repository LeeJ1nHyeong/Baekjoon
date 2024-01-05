from collections import deque

n = int(input())
num_list = []
stack = deque()  # 스택
push_pop = []  # +, - 를 담기 위한 리스트
for _ in range(n):
    number = int(input())
    num_list.append(number)

stack_num = 1
idx = 0  # num_list 인덱스로 활용
is_possible = True  # 제시된 수열이 가능한지에 대한 boolean

while stack_num <= n:

    stack.append(stack_num)
    stack_num += 1
    push_pop.append('+')

    while True:
        # pop될 차례가 아닌데 stack에 존재하면 제시된 수열을 만들 수 없기 때문에
        # is_possible을 False로 설정
        if num_list[idx] != stack[-1]:  
            if num_list[idx] in stack:
                is_possible = False
            break
        stack.pop()
        push_pop.append('-')
        idx += 1

        if not stack:
            break

    if not is_possible:
        break

if not is_possible:
    print("NO")
else:
    for p in push_pop:
        print(p)