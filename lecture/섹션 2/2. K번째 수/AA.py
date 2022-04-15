t = int(input())
for case in range(t):
    n, s, e, k = map(int, input().split())
    caselist = list(map(int, input().split()))
    x = caselist[s-1:e]
    x.sort()
    print(f'#{case+1} {x[k-1]}')
