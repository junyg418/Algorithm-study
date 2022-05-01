'''
Chapter 05 DFS/BFS
2022-04-12-22:43
알고리즘 책 149p
음료수 얼려 먹기|난이도 중하|풀이시간 30분|
DFS
1.문제 해설->코드작성
2.코드복습->해설코드작성
3.문제풀이->정답(해설코드)
'''
n, m = map(int, input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x>=n or x<=-1 or y>=m or y<=-1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        return True
    return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            cnt +=1

print(cnt)