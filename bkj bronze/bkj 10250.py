'''
ACM 호텔(10250)b3
2022-06-21 
1.실패
8.성공
'''
import sys
test_case = int(sys.stdin.readline().strip())
# test_case = 1
for _ in range(test_case):
    H, W, N = map(int, sys.stdin.readline().split())
    # H : 층수, W : 각 층의 방 개수, N : 몇 번째 손님

    XX = N//H+1 # 호수 
    if H>N:
        XX = 1
    if N%H == 0:
        XX -=1

    YY = N%H
    if not YY:
        YY = H
    print(f'{YY}{str(XX).zfill(2)}')  # 문자열 앞  f 는 f-string. format 하고 같은것이니 파이썬에서는 되게 유용
    #zfill() 첫번째 인자만큼의 글자 개수까지 현재 문자열의 길이에서 부족한 공간을 앞부분을 0으로 채움 