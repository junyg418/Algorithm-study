#2023-04-22 16:30 5분컷

n = int(input())

count = 0

for hour in range(n+1):
    for minute in range(60):
        for sec in range(60):
            if '3' in f"{hour}{minute}{sec}":
                count += 1

print(count)