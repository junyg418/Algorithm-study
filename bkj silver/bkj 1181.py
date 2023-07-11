n = int(input())
keys = [input() for _ in range(n)]

keys = list(set(keys))
keys.sort()
keys.sort(key=len)
for key in keys:
    print(key)