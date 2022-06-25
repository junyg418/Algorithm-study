'''
숫자의 개수(2577)b2
2022-06-25
1.
'''
# dic = {}
# for i in range(10):
#     dic[input()] = 0
# print(dic)
a = int(input())
b = int(input())
c = int(input())
sum_value  = str(a*b*c)

count = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for val in sum_value:
    count[val] += 1
for i in range(10):
    print(count[str(i)])