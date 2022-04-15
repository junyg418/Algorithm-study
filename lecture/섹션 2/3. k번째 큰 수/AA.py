n, k = map(int, input().split())
value = list(map(int, input().split()))
value.sort()
resu = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            yo = value[i]+value[j]+value[m]
            resu.add(yo)
res = list(resu)
res.sort(reverse=True)
print(res[k-1])
