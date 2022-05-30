'''
터렛(1002)S4
2022-05-30-22:42
1.틀렸습니다.
2.틀렸습니다.
3.런타입에러
4.틀렸습니다.
5.성공
'''
from math import sqrt


Testcase = int(input())
for _ in range(Testcase):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d  = sqrt((x2-x1)**2 + (y2-y1)**2)
    r_range = r1+r2
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif d>r_range or d < abs(r1-r2):
        print(0)
    elif d == r_range or d == abs(r1-r2):
        print(1)
    elif d< r_range:
        print(2)
