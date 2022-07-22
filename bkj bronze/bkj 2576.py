'''
홀수(2576)b2
2022-07-22
1.정답
'''
hol = []
for _ in range(7):
    num = int(input())
    if num%2:
        hol.append(num)
if len(hol):
    print(sum(hol))
    print(min(hol))
else:
    print(-1)