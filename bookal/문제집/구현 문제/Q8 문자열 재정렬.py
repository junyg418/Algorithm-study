'''
문자열 재정렬(322p)
풀이시간 20분
2022-05-14-13:12
1.입력예시 2개 정답 -> 18분소요
'''
import re
s = ' '.join(input())

values = s.split(' ')
values.sort()
str_start = 0
for idx, i in enumerate(values):
    if not i.isdigit():
        str_start = idx
        break
int_var = sum(list(map(int, values[:str_start])))
str_var = ''.join(values[str_start:])+str(int_var)
print(str_var)