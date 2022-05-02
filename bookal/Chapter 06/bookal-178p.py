'''
Chapter 06 정렬
2022-05-02-20:54
알고리즘 책 178p
위에서 아래로|난이도 하|풀이시간 15분|
1.3분
'''
import sys
n = int(input())

array = []
for _ in range(n):
    array.append(sys.stdin.readline())

array.sort(reverse=True)

for i in array:
    print(array, end=' ')