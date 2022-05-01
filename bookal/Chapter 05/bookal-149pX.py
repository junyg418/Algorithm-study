'''
Chapter 05 DFS/BFS
2022-04-12-22:43
알고리즘 책 113p
음료수 얼려 먹기|난이도 중하|풀이시간 30분|
DFS
1.문제 해설->코드작성
2.코드복습->해설코드작성
'''
import sys

sys.stdin = open('input.txt')
n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

def dfs(x, y):
    if x>=n or x<=-1 or y>=m or y<=-1:
        return False
    if maps[x][y] == 0:
        maps[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y) == True:
            result +=1

print(result)