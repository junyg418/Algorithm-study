n = int(input())
stu = list(map(int, input().split()))

per = int(sum(stu)/(len(stu)) +0.5)

minx = float('INF')
for idx, i in enumerate(stu, 1):
    tmp = abs(per-i)
    if tmp < minx:
        minx = tmp
        score = i
        index = idx
    elif tmp == minx:
        if i>score:
            score = i
            index = idx


print(per, index)