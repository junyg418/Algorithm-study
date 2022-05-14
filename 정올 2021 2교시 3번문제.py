'''
정올 2021 2교시 3번문제
2022-05-14-21:58
1. 예제 맞았지만 점수 0점
'''

import sys

# sys.stdin = open('input')
testcase = int(input())
alpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','s','y','z']
for _ in range(testcase):
    alpas = []
    x = input()
    y = input()
    w = input()
    x_idx = []
    y_idx = []
    for idx, i in enumerate(w[::-1]):
        if not idx:
            x_idx.append(x.rfind(i))
            y_idx.append(y.rfind(i))
        else:
            x_idx.append(x[:x_idx[idx-1]].rfind(i))
            y_idx.append(y[:y_idx[idx-1]].rfind(i))
    x_idx.reverse()
    y_idx.reverse()
    breaker = False
    for alpa in alpabet:
        if alpa in x and alpa in y:
            alpas.append(alpa)
    for i in range(len(w)):
        for alpa in alpas:
            if not i:
                x_pos = x[:x_idx[i]].find(alpa)
                y_pos = y[:y_idx[i]].find(alpa)
                # if x[:x_idx[i]].find(alpa) != -1 and y[:y_idx[i]].find(alpa) != -1:
                if x_pos != -1 and y_pos != -1:
                    print(1)
                    breaker = True
                    continue
            else:
                x_pos =  x[x_idx[i-1]+1:x_idx[i]].find(alpa)
                y_pos =  y[y_idx[i-1]+1:y_idx[i]].find(alpa)
                # if x[x_idx[i-1]+1:x_idx[i]].find(alpa) != -1 and y[y_idx[i-1]+1:y_idx[i]].find(alpa) != -1:
                if x_pos != -1 and y_pos != -1:
                    print(1)
                    breaker = True
                    break
        if breaker:
            break
    else:
        print(0)
