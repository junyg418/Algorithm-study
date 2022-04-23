'''
부녀회장이 될테야(2775)b1
푼 날자:2022-04-19-11:40
1.실패
2.답지->수정,이해
'''
import sys
t = int(input())

for _ in range(t):
    floor= int(sys.stdin.readline())
    num = int(sys.stdin.readline())
    apt = [x for x in range(1, num+1)]
    # 1 4 10
    # 1 3 6
    # 1 2 3
    for j in range(floor):
        for i in range(1, num):
            apt[i] += apt[i-1]
    print(apt[-1])
