n, m = map(int, input().split())
group = {}  # 걸그룹 목록
member = {}  # 멤버

for _ in range(n):
    group_name = input()
    member_cnt = int(input())
    members = []

    # 걸그룹 멤버들의 이름을 members 리스트에 저장하고 이름을 key, 그룹명을 value로 하여 member 해쉬에 저장
    for _ in range(member_cnt):
        name = input()
        members.append(name)
        member[name] = group_name

    # members 리스트 오름차순 정렬 후 그룹명을 key, 멤버 리스트를 value로 하여 group 해쉬에 저장
    members.sort()
    group[group_name] = members

for _ in range(m):
    quiz = input()
    quiz_type = int(input())

    # quiz_type이 0일 경우 group 해쉬에서 그룹명을 key로 갖는 리스트 내의 멤버들 출력
    if quiz_type == 0:
        for mem in group[quiz]:
            print(mem)
    # quiz_type이 1일 경우 member 해쉬에서 멤버명을 key로 갖는 그룹명 출력
    elif quiz_type == 1:
        print(member[quiz])
