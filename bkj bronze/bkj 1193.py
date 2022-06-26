'''
분수찾기(1193)b1
2022-06-26
1.
'''
x = int(input())
stack = 1
while stack < x:
    x -= stack
    stack += 1
if stack%2==0: #짝수

    print(f'{x}/{stack-x+1}')
else: # 홀수 
    print(f'{stack-x+1}/{x}')