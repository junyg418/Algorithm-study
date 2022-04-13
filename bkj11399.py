'''
ATM(11399번)
-분류 그리드알고리즘
정답 비율:	66.763%
푼 날자: 2022-04-13-23:38
1.수정후 정답
'''
n = int(input())
time = list(map(int, input().split()))
time.sort()
pertime = 0
an = 0
for i in time:
    an += i
    pertime += an
print(pertime)