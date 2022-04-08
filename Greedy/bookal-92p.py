'''
탐욕 알고리즘
2022-04-08
알고리즘 책 92P
큰 수의 법칙 난이도 하
1. 1회 오답, 수정후 정답-(30:00)
-주석
    한번 k번 사용된 인덱스는 사용이 안된다 이해함
    즉 문제 잘 안읽음
'''

# 1차 작성
# n, m, k = map(int, input().split())
# li = list(map(int, input().split()))
# li.sort(reverse=True)
# cnt = 0
# circle = 0
# for num in range(n): 
#     for _ in range(k):
#         if circle <= m:
#             cnt += li[num]
#             circle += 1
#         else:
#             break
# print(cnt)

# 2차 작성 정답
# n, m, k = map(int, input().split())
# li = list(map(int, input().split()))
# li.sort(reverse=True)
# cnt = 0
# circle = 0
# while circle < m:
#     for _ in range(k):
#         if circle < m:
#             cnt += li[0]
#             circle+=1
#         else:
#             break
#     if circle < m:
#         cnt += li[1]
#         circle += 1
#     else:
#         break
# print(cnt)

#3차 추가 아이디어 정답 (약 5:00)
n, m, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
first_val = li[0]
second_val = li[1]
cnt = int(first_val*k*(m/(k+1))+second_val*(m/(k+1)))

print(cnt)

