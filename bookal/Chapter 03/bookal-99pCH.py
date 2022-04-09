'''
2022-04-08
알고리즘 책 99P
1이 될 때까지 난이도 하
1.예시 통과-(8:38)
'''
n, k = map(int, input().split())
cnt = 0
while n != 1: #1이 될 때까지 반복
    if not n%k: #나머지 연산자를 이용해 나머지값이 0이면 n을 k로 나눈다
        n/=k
        cnt+=1
    else:      
        n -= 1
        cnt+=1
print(cnt)