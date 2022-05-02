'''
Chapter 07 이진 탐색
2022-05-03-00:02
알고리즘 책 197p
부품 찾기|난이도 중하|풀이시간 30분|
1. 10분컷 유후~~
'''
import sys
sys.stdin = open('input')
sys.setrecursionlimit(10**8)
n = int(input())  # 전체 물건 개수
array = list(map(int, sys.stdin.readline().split()))  #부품의 고유번호들

m = int(input()) # 필요 부품 개수
targets = list(map(int, sys.stdin.readline().split())) # 찾고자 하는 물품의 번호

def binary_serach(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_serach(array, target, 0, mid-1)
    else:
        return binary_serach(array, target, mid+1, end)

for target in targets:
    if binary_serach(array, target, 0, n-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
