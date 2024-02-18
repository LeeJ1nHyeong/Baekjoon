from collections import deque
import sys
input = sys.stdin.readline


def bfs():  # bfs
    a, b = map(int, input().split())
    queue = deque([(a, '')])
    visited = [0] * 10000  # 메모리 사용을 줄이기 위해 0 ~ 9999까지의 값 방문 여부 체크

    while True:
        current, command = queue.popleft()

        # DSLR 별로 return한 값이 미방문이라면 방문 체크 후 queue에 담기
        # return값이 b라면 명령어 return
        if d(current) == b:
            return command + "D"
        if not visited[d(current)]:
            visited[d(current)] = 1
            queue.append((d(current), command + "D"))

        if s(current) == b:
            return command + "S"
        if not visited[s(current)]:
            visited[s(current)] = 1
            queue.append((s(current), command + "S"))

        if l(current) == b:
            return command + "L"
        if not visited[l(current)]:
            visited[l(current)] = 1
            queue.append((l(current), command + "L"))

        if r(current) == b:
            return command + "R"
        if not visited[r(current)]:
            visited[r(current)] = 1
            queue.append((r(current), command + "R"))


def d(num):  # D - 현재 값의 2배를 return, 9999를 넘기면 10000을 나눈 나머지 값 return
    num *= 2
    if num > 9999:
        return num % 10000
    return num


def s(num):  # S - 현재 값에 1을 뺀 값을 return, 0이라면 9999 return
    if num == 0:
        return 9999
    num -= 1
    return num


def l(num):  # L - 현재 값의 각 자리 순서를 2341로 변환하여 return, 0도 고려하여 진행
    num = ((num * 10) + num // 1000) % 10000
    return num


def r(num):  # R - 현재 값의 각 자리 순서를 4123으로 변환하여 return, 0도 고려하여 진행
    num = (num // 10) + (num % 10) * 1000
    return num


t = int(input())

for _ in range(t):
    print(bfs())
