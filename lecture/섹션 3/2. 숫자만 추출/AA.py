import re
# import sys
# sys.stdin = open('input.txt')
value = input()
ak = re.findall('[0-9]', value)
num = int(str.join('', ak))
print(num)
cnt = 0
for i in range(1, num+1):
    if not num%i:
        cnt +=1
print(cnt)