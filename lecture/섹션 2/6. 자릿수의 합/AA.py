n = int(input())
val = list(map(int, input().split()))
def digit_sum(x):
    value = 0
    for i in str(x):
        value += int(i)
        return x, value

result = {}
for k in val:
    key, value = digit_sum(k)
    result[value] = key

print(result[max(result)])
