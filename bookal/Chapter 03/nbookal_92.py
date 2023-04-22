# 2023-04-22 15:12 check
n, m, k= map(int, input().split())
input_list = sorted([int(input()) for _ in range(n)], reverse=True)

count = 1
result = 0
for _ in range(m):
    if count % (k+1)==0:
        result += input_list[1]
    else:
        result += input_list[0]
    count +=1
print(result)