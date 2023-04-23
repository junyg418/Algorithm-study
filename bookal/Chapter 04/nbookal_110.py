# 2023-04-22 16:16 9분 컷
# direct = [0, 1, 2, 3] 
n = int(input())
direct_list = input().split()

location = [1, 1]

for dircet in direct_list:
    if dircet == "L":
        if location[1] == 1:
            pass
        else:
            location[1] += -1

    elif dircet == "R":
        if location[1] == n:
            pass
        else:
            location[1] += 1

    elif dircet == "U":
        if location[0] == 1:
            pass
        else:
            location[0] += -1

    elif dircet == "D":
        if location[0] == n:
            pass
        else:
            location[0] += 1

print(" ".join(list(map(str, location))))