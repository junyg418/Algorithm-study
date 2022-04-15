n, m = map(int, input().split())
result = {}
for ns in range(1,n+1):
    for ms in range(1,m+1):
        if not ns+ms in result:
            result[ns+ms] = 1
        else:
            result[ns+ms] += 1
answer = []
for i in result:
    if result[i] == max(result.values()):
        answer.append(str(i))
print(str.join(' ', answer))
