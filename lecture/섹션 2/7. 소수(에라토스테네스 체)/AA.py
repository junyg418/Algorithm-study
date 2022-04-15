n = int(input())
lists = []
def checker(k):
    global lists
    # print(f'lists:{lists},k:{k}')
    for i in lists:
        if not k%i:
            return False
    return True

for i in range(2,n+1):
    if checker(i):
        lists.append(i)

print(len(lists))