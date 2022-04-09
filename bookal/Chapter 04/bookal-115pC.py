'''
Chapter 04 구현
2022-04-10-03:31
알고리즘 책 113p
왕실의 나이트|난이도 하|풀이시간 20분|
1. 해결-(14:18)
'''
data = input()
eng = ['a','b','c','d','e','f','g','h']
pose = [0, 0]
cnt = 0

pose[0] = eng.index(data[0])+1
pose[1] = int(data[1])

poseUL = [pose[0]-2,pose[1]-1]
poseUR = [pose[0]-2,pose[1]+1]
poseDL = [pose[0]+2,pose[1]-1]
poseDR = [pose[0]+2,pose[1]+1]

poseaa = [pose[0]-1,pose[1]-2]
posebb = [pose[0]-1,pose[1]+2]
posecc = [pose[0]+1,pose[1]-2]
posedd = [pose[0]+1,pose[1]+2]


poses = [poseUL,poseUR,poseDL,poseDR,poseaa,posebb,posecc,posedd]
def check(value):
    global cnt
    if 0< value[0] <9:
        if 0<value[1]<9:
            cnt+=1
for i in poses:
    check(i)
print(cnt)
