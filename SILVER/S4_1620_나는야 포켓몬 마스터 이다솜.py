import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 딕셔너리
pokemons = {}  # key 번호, value 포켓몬
numbers = {}  # key 포켓몬, value 번호

for i in range(1, n + 1):
    pokemon = input().rstrip()
    pokemons[i] = pokemon
    numbers[pokemon] = i

# m개의 문제
for _ in range(m):
    quiz = input().rstrip()
    # 문제가 숫자라면 pokemons 딕셔너리에서 해당 key의 value 출력
    if quiz.isdigit():
        print(pokemons[int(quiz)])
    # 숫자가 아니라면 numbers 딕셔너리에서 해당 key의 value 출력
    else:
        print(numbers[quiz])