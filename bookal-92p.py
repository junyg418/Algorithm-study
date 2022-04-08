'''
알고리즘 책 92P
큰 수의 법칙 난이도 하
1. 1회 오답, 수정후 정답(30:00)
-주석
    한번 k번 사용된 인덱스는 사용이 안된다 이해함
    즉 문제 잘 안읽음
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