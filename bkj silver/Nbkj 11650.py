'''
좌표 정렬하기(11650)S5
푼 날자:2022-04-17-02:41(4분소요)
        2022-04-17-12:21(2분)- 정렬 학습후 다시 풀이

'''
import sys
sys.stdin = open('input.txt')
n = int(input())
datas = []

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    datas.append(data)

# datas.sort()
print(data)