'''
단어의 개수(1037)b1
2023-05-02
1.성공 ??
'''
count = int(input())
if count ==1:
    n = int(input())
    print(n*n)
else:
    input_list = list(map(int, input().split()))
    min_value = min(input_list)
    max_value = max(input_list)
    print(min_value*max_value)