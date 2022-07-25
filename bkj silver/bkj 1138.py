'''
한 줄로 서기(1138)s2
2022-07-25
1.
'''
from turtle import pos


man_count = int(input())
hight_info_list = list(map(int, input().split()))

success_idx_list = [0 for _ in range(man_count)]

def zero_counter(value):
    pos = 1
    while True:
        if answer[:pos].count(0) >= value:
            return pos
        pos +=1


answer = [0 for _ in range(man_count)]
for count, count_num in enumerate(hight_info_list):
    success = True
    pos = zero_counter(count_num)

    while success:
        if pos not in success_idx_list:
            answer[pos] = count+1
            success_idx_list[count] = count_num

            success = False
                
        else:
            pos+=1
print(success_idx_list)