# 2023-06-09

n = int(input())
real_sc = list(map(int, input().split()))
c_sc = list(map(lambda x:x/max(real_sc)*100, real_sc))    
print(sum(c_sc)/n)