n = int(input())

array = [[0 for _ in range(n)] for _ in range(n)]

alpa = 65
for i in range(n):
    for j in range(n):
        array[n-j-1][n-i-1] = chr(alpa)
        alpa+=1
        if alpa >= 91:
            alpa = 65

for i in array:
    for j in i:
        print(j, end=" ")
    print()