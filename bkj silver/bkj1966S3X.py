'''
프린터 큐(1966)S3
푼 날자:2022-04-17-12:26
1.실패(1시간 2분)
-문제
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이  "문서를 인쇄하지 않고"   Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
에서 문서를 인쇄를 하지 않고라는 의미를 빠뜨려, 카운트를 세고 max값 문서를 인쇄했기에 풀지 못하였다.

2.정답지보고 이해하면서 풀이
continue, break 차이점 복습필요
'''
from collections import deque
import sys
# sys.stdin = open('input.txt')
n = int(input())
for _ in range(n):
    n, m = map(int, sys.stdin.readline().split())
    value = deque(map(int, sys.stdin.readline().split()))
    cnt = 0
    while value:
        maxval = max(value)
        first = value.popleft()
        m -=1
        if first == maxval:
            cnt +=1
            if m < 0:
                print(cnt)
                break
        else:
            value.append(first)
            if m< 0:
                m = len(value)-1
#1차시도
# from collections import deque
# import sys
# sys.stdin = open('input.txt')
# n = int(input())
# for _ in range(n):
#     que, where = map(int, sys.stdin.readline().split())
#     value = deque(map(int, sys.stdin.readline().split()))
#     cnt = 0
#     for __ in range(que):
#         if value[0] < max(value):
#             value.append(value[0])
#             value.popleft()
#             value.remove(max(value))
#             cnt += 1
#             if not where:
#                 where = que-1
#             else:
#                 where -= 1
#         else:
#             if not where:
#                 cnt+=1
#                 print(cnt)
#                 continue
#             else:
#                 value.popleft()
#                 cnt+=1
#     if cnt - 1 ==0:
#         continue
#     else:
#         print(cnt-1)