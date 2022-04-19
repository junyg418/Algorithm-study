'''
부녀회장이 될테야(2775)b1
푼 날자:2022-04-19-11:40
1.
'''
t = int(input())

for _ in range(t):  
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]
    for k in range(floor):
        for i in range(1, num):
            f0[i] += f0[i-1]
    print(f0[-1])