'''
Chapter 06 정렬
2022-05-02-21:22
알고리즘 책 182p
두 배열의 원소 교체|난이도 하|풀이시간 20분|
1.6분 소요 정답
'''
n, k = map(int, input().split())
Aarray = list(map(int, input().split())).sort()
Barray = list(map(int, input().split())).sort(reverse=True)

for i in range(k):
    if Aarray[i] < Barray[i]:
        Aarray[i], Barray[i] = Barray[i], Aarray[i]
    else:
        break

print(sum(Aarray))