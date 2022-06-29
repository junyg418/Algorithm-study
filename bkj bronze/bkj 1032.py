'''
명령 프롬프트(1032)b1
2022-06-29
1.성공
'''
case = int(input())
answer = []
val = input()
for st in val:
    answer.append(st)
for _ in range(case-1):
    val = input()
    for idx, st in enumerate(val):
        if answer[idx] == st:
            pass
        else:
            answer[idx] = '?'
print(''.join(answer))