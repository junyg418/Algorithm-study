'''
Java 카카오 코딩테스트- 다트 게임
https://goyunji.tistory.com/79
2022-05-20-16:29
'''

result = []
num = ''
for idx, val in enumerate(input_val:=input()):
    if val.isdigit():
        num = num + val
    elif val.isalpha():
        if val == 'S':
            result.append(int(str(num)+'1'))
            num = ''
        elif val == 'D':
            result.append(int(str(num)+'2'))
            num = ''
        elif val == 'T':
            result.append(int(str(num)+'3'))
            num = ''
    elif val == '*':
        for i in range(len(result)):
            result[i] = result[i]*2
    elif val == '#':
        result[-1] = result[-1]*-1
value = 0
for i in result:
    value += i
print(value)
