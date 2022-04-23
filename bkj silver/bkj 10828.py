'''
스택(10828) S4
푼 날자: 
1차 2022-04-17-01:39
-시간초과 실패->성공(39분 걸림)
import sys
sys.stdin.readline()
->여러줄을 계속 input 받아야할때-> 사용 시간 매우 단축
'''
import sys
n = int(input())

def checker(do):
    global stack
    if 'push' in do:
        stack.append(do.split()[1])
    if 'pop' in do:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    if 'size' in do:
        print(len(stack))
    if 'empty' in do:
        if not stack:
            print(1)
        else:
            print(0)
    if 'top' in do:
        if not stack:
            print(-1)
        else:
            print(stack[-1])

stack = []
for _ in range(n):
    doit = sys.stdin.readline()
    checker(doit)