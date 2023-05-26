k = int(input())
result = [list(map(int, input().split())) for _ in range(k)]

result.sort(key=lambda x:(x[1], x[0]))
for i in result:
    print(" ".join(map(str, i)))