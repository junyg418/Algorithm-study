'''
분산처리(1009)B2
2022-07-21
1. 시간초과
2.....
7. 성공
총평:
시간단축 필요함, 살짝 어렵다
'''
###### case 1 ######
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     num = a**b
#     print(str(num)[-1])

###### case 2 ######
for _ in range(int(input())):
    a, b = map(int, input().split())
    num = a**(4 if not b%4 else b%4)
    print(10 if str(num)[-1] == '0' else str(num)[-1])