'''
제로(10773)S4
2023-05-24
1.
'''
k = int(input())
stack = []
for _ in range(k):
    input_data = int(input())
    if input_data == 0:
        stack.pop()
        continue
    stack.append(input_data)

print(sum(stack))