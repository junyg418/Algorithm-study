'''
알고리즘 책 92P
큰 수의 법칙 난이도 하
'''

n, m, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
cnt = 0
circle = 0
# print(li)
# for num in range(n): 
#     for _ in range(k):
#         if circle <= m:
#             cnt += li[num]
#             circle += 1
#         else:
#             break
# print(cnt)

while circle < m:
    for _ in range(k):
        if circle < m:
            cnt += li[0]
            circle+=1
        else:
            break
    if circle < m:
        cnt += li[1]
        circle += 1
    else:
        break
print(cnt)