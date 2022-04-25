'''
점프왕 최준민(11564)
2022-04-25-15:23
1.실패 -> 틀렸습니다.
2.틀렸습니다.
3.풀이확인 틀렸습니다.
'''


k, a, b = map(int, input().split())
choloate = 0
if (a<0 and b>0) or (a>0 and b<0):
    if a<0:
        a = -a
    if b<0:
        b = -b
    print(int(b/k + a/k+1))

else:#a와 b사이에 0이 포합되어있을 때
    a = abs(a)
    b = abs(b)
    if a>b:
        c = a
        a = b
        b = c
    choloate = b/k - a/k
    if a % k  ==0:
        choloate +=1
    print(int(choloate))

# cnt = 0
# if a<0 and b<=0:   #둘다 음수일때
#     cnt += (-a//k) - ((-b -1)//k)
# elif a<0 and b>0:
#     cnt += (-a//k) + (b//k)
# elif a>=0 and b>0:
#     cnt += (b//k) - ((a -1)//k)
# if a<=0 and 0<=b:
#     cnt+=1

# print(cnt)


#1차 시도
# k, a, b = map(int, input().split())
# line = b-a+1
# chocolate = line//k
# if a<=0 and 0<=b:
#     chocolate+=1
# print(chocolate)