'''
성 지키기(1236)b1
2022-10=10
1.
'''
size = list(map(int, input().split()))
# info = []
# for _ in range(size[1]):
#     info.append(input().split())
info = [input().split() for _ in range(size[1])]

count = 0
non_seroIdx = []
# 세로줄 학인
for idx in range(size[1]):
    for cnt in range(size[0]):
        if info[cnt][idx] == 'X':
            break
    else:
        non_seroIdx.append(idx)
        count += 1
# 가로줄 모두 확인
for idx in range(size[0]):
    if 'X' in info[idx]:
        pass
    else:
        for idx in range()



print (count)
