'''
Chapter 08 다이나믹 프로그래밍
2022-05-06-13:38
알고리즘 책 217p
1로 만들기|난이도 중하|풀이시간 20분|
1.설명보고 풀이
'''
x = int(input())

d = [0]*30001
for i in range(2,x+1):
    d[i] = d[i-1] + 1
    if i % 2 ==0 :
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])