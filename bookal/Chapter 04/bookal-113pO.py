'''
Chapter 04 구현
2022-04-10-01:36
알고리즘 책 113p
시각|난이도 하|풀이시간 15분|
1.오답-(6:00)
    -3을 세는 방법을 잘못함
        3이 포함되어있을 때를 카운트하지 않음
        3만 있을때 카운트함
2.정답-(5:43)
    -46번째줄 풀이 보고 함
'''
#1번 풀이
# hour = int(input())
# cnt =0
# time = [0,0,0]

# while not time == [hour,59,59]:
#     if time[1] == 60:
#         time[1] = 0
#         time[0] += 1
#     if time[2] == 60:
#         time[2] = 0
#         time[1] += 1
    
#     if time.count(3)>=1:
#         cnt += 1
#     time[2]+=1
#     print(time)
# print(cnt) 6분



#2번풀이
hour = int(input())
cnt =0
time = [0,0,0]

while not time == [hour,59,59]:
    if time[1] == 60:
        time[1] = 0
        time[0] += 1
    if time[2] == 60:
        time[2] = 0
        time[1] += 1
    
    if '3' in str(time[0])+str(time[1])+str(time[2]):
        cnt += 1
    time[2]+=1
print(cnt)
