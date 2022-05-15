'''
한조서열정리하고옴ㅋㅋ(14659)
2022-05-12-13:50-14:04
1.예제 정답-> 체점 틀림
'''
import sys
sys.stdin = open('input')
n = int(sys.stdin.readline())
highs = list(map(int, sys.stdin.readline().rstrip().split()))

result = []
for i in range(n):
    shooter = highs[i]
    cnt = 0
    for j in highs[i+1:]:
        if shooter >= j:
            cnt+=1
    result.append(cnt)
print(max(result))