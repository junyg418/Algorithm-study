'''
마인크래프트(18111)S2
푼 날자:2022-04-20-12:15
1.시간초과
2.틀렸습니다
3.풀이확인
'''
n, m, b = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

mintime = float('INF')
tall = 0
for i in range(267):
    Max = 0
    Min = 0
    for j in range(n):
        for k in range(m):
            if maps[j][k] < i:
                Min += (i - maps[j][k])
            else:
                Max += (maps[j][k] - i)
    inventory = Max + b
    if inventory < Min:
        continue
    time = 2*Max + Min
    if time <= mintime:
        mintime = time
        tall = i
print(mintime, tall)


#1, 2차시도
# import sys
# sys.stdin = open('input.txt')
# n, m, b = map(int, sys.stdin.readline().split())

# maps = [] #지도 생성
# for _ in range(n):
#     maps.append(list(map(int, sys.stdin.readline().split())))

# sums = 0
# for i in maps:
#     sums += sum(i)
# average = int(sums/(n*m)+0.5)

# inventory = b
# time = 0

# def checker(maps): #지도의 평균값이 아닌 값이 있나 확인
#     global average
#     for i in maps:
#         for j in i:
#             if not j == average:
#                 return True
#     return False

# while checker(maps):
#     cnt = 0
#     for i in maps: #필요한 블럭 개수 ->cnt
#         for j in i:
#             cnt += j - average
#     if inventory + cnt < 0: #가지고 있는 블럭 개수 작을때 
#         average -= 1
#         continue
    
#     for x, i in enumerate(maps): #블럭 놓고 제거
#         for y, j in enumerate(i):
#             if j < average:
#                 # for _ in range(average -j):
#                 time += 1*(average -j)
#                 inventory -= 1*(average -j)
#                 maps[x][y] += 1*(average -j)
#             elif j> average:
#                 # for _ in range(j - average):
#                 time += 2*(j - average)
#                 inventory += 1*(j - average)
#                 maps[x][y] -= 1*(j - average)
# print(f'{time} {average}')