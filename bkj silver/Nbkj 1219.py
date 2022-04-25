'''
소수 구하기(1929)S3
푼 날자: 2022-04-24-00:51
1.시간초과 - 에라토스테네스의 체를 알아야함 (11분)
'''
n, m = map(int, input().split())
primenums = []
# stack = [i for i in range(n,m+1)]
for num in range(n, m+1):
    if not num%2:
        continue
    for prime in primenums:
        if not num%prime:
            break
    else:
        primenums.append(num)
if n == 2 or n== 1:
    primenums.insert(0,2)
print(primenums)