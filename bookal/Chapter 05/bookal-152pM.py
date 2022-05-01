'''
Chapter 05 DFS/BFS
2022-05-01-11:20
알고리즘 책 149p
미로 탈출|난이도 중하|풀이시간 30분|
BFS
1.풀이보고해결
'''
from collections import deque
import sys

sys.stdin = open('input')
n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input())))

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y)) #풀이참조
    while queue: #풀이참조
        x, y = queue.popleft()
        for i in range(4):
            print(queue)
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[n-1][m-1]
print(bfs(0,0))