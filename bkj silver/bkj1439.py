'''
뒤집기(1439)S5
푼 시간:2022-04-22
'''
import sys
strval = sys.stdin.readline().rstrip()
stack = {'0':0,'1':0}
for idx, i in enumerate(strval[1:], 1):
    if i == strval[idx-1]:
        pass
    else:
        stack[strval[idx-1]] +=1
print(stack['0'] if stack['0']>stack['1'] else stack['1'])