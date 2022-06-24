'''
알파벳 개수(10808)b4
2022-06-23
1.10분컷
'''

# dic = {}
# for _ in range(36):
#     a = input()
#     dic[a] = 0
# print(dic)
# a b c d e ~ z를 입력하여 딕셔너리 쉽게 만듦
# -------------------

s = input()
dic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 
'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

for string in s:
    dic[string] += 1

for num in dic.values():
    print(num, end=' ')

# 다른방법(제자씨 제작)
# a=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
# "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# ex=[]
# s=input()
# for i in s:
#     ex.append(i)
# for i in a:
#     print(ex.count(i),end="")
