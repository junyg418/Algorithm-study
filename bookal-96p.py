'''
알고리즘 책 96P
숫자 카드게임 난이도 하
1.예시 통과-(9:41)
'''
n, m = map(int, input().split())
key = 0
for _ in range(n):
    line = list(map(int, input().split()))
    value = min(line)
    if key < value:
        key = value
print(key)