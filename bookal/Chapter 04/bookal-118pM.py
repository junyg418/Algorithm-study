'''
Chapter 04 구현
1차 2022-04-10-04:57~6:16
2차
알고리즘 책 118p
게임 개발|난이도 중|풀이시간 40분|
1차 실패-(75분)
'''
# n, m = map(int, input().split())
# pos = []
# pos[0],pos[1],d = list(map(int, input().split()))
# # place = [[]*n for _ in range(m)]

# place = []
# for _ in range(m):
#     line = list(map(int, input().split()))
#     place.append(line)

# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# def whatleft():
#     global pos
#     global place
#     global d
#     leftpos = 0
#     if d == 0:
#         leftpos = place[pos[0]-1][pos[1]]  #북
#     elif d == 1:
#         leftpos = place[pos[0]][pos[1]-1]  #동
#     elif d == 2:
#         leftpos = place[pos[0]+1][pos[1]]  #남
#     elif d == 3:
#         leftpos = place[pos[0]][pos[1]+1]  #서
#     return leftpos

# def whatback():
#     global pos
#     global place
#     global d
#     backpos = 0
#     if d == 0:
#         backpos = place[pos[0]][pos[1]+1] 
#     elif d == 1:
#         backpos = place[pos[0]-1][pos[1]] 
#     elif d == 2:
#         backpos = place[pos[0]][pos[1]-1] 
#     elif d == 3:
#         backpos = place[pos[0]+1][pos[1]] 
#     return backpos

# def turn():
#     global d
#     if d == 0:
#         d = 3
#     else:
#         d-1

# def move():
#     if whatleft() != 'x':
#         turn()
#         move()
#     elif whatleft() == 0:
#         turn()
#         pos[0] = pos[0]+dx[d]
#         pos[1] = pos[1]+dx[d]
#         place[pos[0]][pos[1]] = '1'
#         move()
#     elif whatleft == 1:

