'''
Chapter 04 구현
2022-04-10-01:00
알고리즘 책 110P
상하좌우|난이도 하|풀이시간 15분|
1.예시 통과(15:30풀이시간 초과)
'''
n = int(input())
pose = [1,1]
def change(k):
    global pose
    if k == 'L':
        if pose[1] == 1:
            pass
        else:
            pose[1] += -1

    elif k == 'R':
        if pose[1] == n:
            pass
        else:
            pose[1] += 1

    elif k == 'U':
        if pose[0] == 1:
            pass
        else:
            pose[0] += -1

    elif k == 'D':
        if pose[0] == n:
            pass
        else:
            pose[0] += 1


movelog = list(input().split())
for k in movelog:
    change(k)
x, y = pose
print(x, y)