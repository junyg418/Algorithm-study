n :int= int(input())
stage_count:list[int] = list(map(int, input().split()))
b, c = map(int, input().split())

result = n

for value in stage_count:
    value += -b
    if value <= 0:
        continue
    asd = value//c
    if value%c ==0:
        result += asd
    else:
        result += (asd+1)
print(result)