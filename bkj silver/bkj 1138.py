'''
한 줄로 서기(1138)s2
2022-07-25
2022-07-26
1.예제 성공 but RuntimError
-사유
    join 사용시 answer들의 요소가 int였기에 오류
2.정답
'''
man_count = int(input())
hight_info_list = list(map(int, input().split()))

success_idx_list = [None for _ in range(man_count)]

def zero_counter(value):
    pos = 0
    while True:
        if answer[:pos].count(None) >= value:
            return pos
        pos +=1


answer = [None for _ in range(man_count)]
for count, count_num in enumerate(hight_info_list):
    success = True
    pos = zero_counter(count_num)

    while success:
        if pos not in success_idx_list:
            answer[pos] = count+1
            success_idx_list[count] = pos

            success = False
                
        else:
            pos+=1
# print(' '.join(answer)
print(' '.join(map(str, answer)))