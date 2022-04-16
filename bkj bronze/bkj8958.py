'''
OX퀴즈(8958)b2
푼 날자: 2022-04-16
첫제출 정답
'''
n = int(input())
for _ in range(n):
    treehit = 0
    correctval = []
    testcase = input()
    for value in testcase:
        if value == 'O':
            treehit +=1
            correctval.append(treehit)
        elif value == 'X':
            treehit = 0
            correctval.append(treehit)
    print(sum(correctval))