'''
설탕 배달(2839)b1
2022-05-07-23:04
1.
'''
n = int(input())

result = 0
while n>=0:
    if n%5==0:
        result += n//5
        print(result)
        break
    n -= 3
    result +=1
else:
    print(-1)