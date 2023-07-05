# 5 4 3 2 1
# 5-2 * 2 1
n, k = map(int, input().split())
up = 1
for i in range(1,n+1):
    up*=i

for i in range(1, n-k+1):
    up /= i

for i in range(1, k+1):
    up /= i

print(int(up))