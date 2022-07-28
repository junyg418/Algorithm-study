'''
더하기 사이클(1110)b1
2022-07-28
1.성공
'''
num = int(input())
cnt = 0

def oper(num):
    global cnt
    if len(str(num)) == 1:
        # num = int('0' + str(num))
        result = num
    else:
        result = int(int(str(num)[0]) + int(str(num)[1]))
    answer = int(str(num)[-1]+str(result)[-1])
    cnt += 1
    return answer

copy_num = oper(num)
while num != int(copy_num):
    copy_num = oper(copy_num)
print(cnt)
