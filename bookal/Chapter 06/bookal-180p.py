'''
Chapter 06 정렬
2022-05-02-21:06
알고리즘 책 180p
성적이 낮은 순서로 학생 출력하기|난이도 하|풀이시간 20분|
1.12분
'''
n = int(input())

array = []
for _ in range(n):
    a, b = input().split()
    array.append((a,b))

def secont(x):
    return x[1]
array = sorted(array, key=secont)

for i in array:
    print(i[0], end= ' ')