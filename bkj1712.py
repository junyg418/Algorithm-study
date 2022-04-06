#손익분기전 B4
# a, b, c = map(int, input().split())
# son = a
# cnt = 1
# k= 0
# if b>c:
#     print(-1)
# else:
#     while son>k:
#         son+=b
#         k+=c
#         cnt+=1
#     print(cnt)
a, b, c = map(int, input().split())
if b>c:
    print(-1)
else:
    print(a//(c-b)+1)