# arr = sorted([input() for _ in range(int(input()))])
# for i in arr:
#     print(i)


arr = [0]*10000
for i in range(int(input())):
    tmp = int(input())
    arr[tmp-1] += 1

for i in range(10000):
    if arr[i] != 0:
        for k in range(arr[i]):
            print(i+1)