'''
큐(10845)S4
2022-04-24
3번째 정답->
첫번째
    - push x 의 x의 자릿수가 0~9인줄
두번째
    - push x 의 공백까지 index 취급 받는줄
세번째
    -정답
'''
from collections import deque
import sys

sys.stdin = open('input.txt')
n = int(input())
que = deque()
inputs = sys.stdin.readline
inpdata = ['pu','po','si','em','fr','ba']
for _ in range(n):
    value = inputs().strip()
    idx = inpdata.index(value[:2])
    if idx==1: #pop
        if not que:
            print(-1)
        else:
            remv = que.popleft()
            print(remv)
    elif idx==2: #size
        print(len(que))
    elif idx==3: #
        if que:
            print(0)
        else:
            print(1)
    elif idx==4:
        if not que:
            print(-1)
        else:
            print(que[0])
    elif idx==5:
        if not que:
            print(-1)
        else:
            print(que[-1])
    else:
        que.append(int(value[4:]))