'''
검문(2981)G5
푼 날자: 2022-04-22
1.런타임 에러
2.시간초과
'''
#시간초과 코드
from sys import stdin #dot 연산 최적화

stdin = open('input.txt')
n = int(stdin.readline())
nums = [int(stdin.readline().rstrip()) for _ in range(n)]
    

result = []
for i in range(2, max(nums)+1):   #min -> max로 바꿈 ->시간초과
    stack = list()
    staf = stack.append
    for idx, num in enumerate(nums):
        remain = num%i
        staf(remain)
        if remain != stack[idx-1]:
            break
    else:
        result.append(str(i))
print(' '.join(result))


# 1번시도
# import sys

# sys.stdin = open('input.txt')
# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(sys.stdin.readline().rstrip()))

# result = []
# for i in range(2, min(nums)+1):
#     stack = list()
#     for idx, num in enumerate(nums):
#         remain = num%i
#         stack.append(remain)
#         if len(stack) != 1:
#             if remain != stack[idx-1]:
#                 break
#     else:
#         result.append(i)
# for i in result:
#     print(i,end=' ')