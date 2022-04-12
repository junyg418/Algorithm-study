'''
Chapter 05 DFS/BFS
2022-04-12-22:43
알고리즘 책 113p
음료수 얼려 먹기|난이도 중하|풀이시간 30분|
1.
'''
from unittest import result


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x>= n or y <= -1 or y >=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] =1
        dfs(x-1 ,y)
        dfs(x ,y-1)
        dfs(x+1 ,y)
        dfs(x , y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result +=1

print(result)