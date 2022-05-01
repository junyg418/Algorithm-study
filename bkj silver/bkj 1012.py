'''
유기농 배추(1012)S2
2022-05-01-15:49
1.1시간36분해결

런타임 오류 났었음 but 코드이상x
why -> 제귀함수의 최대깊이설정떄문에
'''

import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open('input')  #지울꺼
testcase = int(input())

def dfs(x, y, mapp):
    #지도 밖으로 나가면 사라짐
    if x<= -1 or y<= -1 or x>=n or y>=m:
        return False
    if maps[x][y] == [1]:
        maps[x][y] = [0]
        dfs(x, y-1, mapp)
        dfs(x, y+1, mapp)
        dfs(x-1, y, mapp)
        dfs(x+1, y, mapp)
        return True
    return False

for i in range(testcase):
    m, n, k= map(int, input().split())
    #testcase마다 맵 생성
    maps = [] 
    for _ in range(n):
        maps.append([[0]for _ in range(m)])
    for __ in range(k):
        y,x = map(int, sys.stdin.readline().split())
        maps[x][y][0] = 1

    #모든 케이스 검사
    cnt = 0 
    for I in range(n):
        for J in range(m):
            if dfs(I,J,maps) == True:
                cnt +=1
    print(cnt)