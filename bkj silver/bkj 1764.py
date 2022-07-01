'''
듣보잡(1764)S4
2022-06-30~2022-07-01
1.시간초과
2.틀렸습니다.
3.틀렸습니다.
4.성공했습니다!!!!! set 함수부분 힌트
'''
# from sys import stdin

# n, m = map(int, input().split())
# donthear = []
# answer = []
# for _ in range(n):
#     donthear.append(stdin.readline().strip())
# for _ in range(m):
#     x=stdin.readline().strip()
#     if x in donthear:
#         answer.append(x)
# print(len(answer))
# for i in answer:
#     print(i)


##### Case2 #####
# from sys import stdin

# n, m = map(int, input().split())
# # f = open('input')
# a = stdin.readlines()
# see, look = a[:n], a[n:]
# answer = list(set(see).intersection(look))
# print(len(answer))
# for _ in answer:
#     print(_.strip())


##### Case3 #####
# from sys import stdin

# n, m = map(int, input().split())
# # f = open('input')
# a = list(map(str.strip, stdin.readlines()))
# see, look = a[:n], a[n:]
# answer = list(set(see).intersection(look))
# print(len(answer))
# for _ in answer:
#     print(_)

##### Case4 #####
from sys import stdin
n, m = map(int, input().split())
a = list(map(str.strip, stdin.readlines()))
see, look = set(a[:n]), set(a[n:])
lists = sorted(list(see & look))
print(len(lists))
for i in lists:
    print(i)