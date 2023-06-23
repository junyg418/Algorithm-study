# alpa = [0 for _ in range(26)]
# value = input()
# for data in value:
#     alpa[ord(data.upper())-65] += 1
# max_value = max(alpa)
# if alpa.count(max_value) != 1:
#     print("?")
# else:
#     print(chr(alpa.index(max_value)+65))

# a, b = map(int, input().split())
# if a>b:
#     print(">")
# elif b>a:
#     print("<")
# else:
#     print("==")

# n = int(input())
# for count in range(1, n+1):
#     print(" "*(n-count),end="")
#     print("*"*count)

# print(input()[int(input())-1])

# print(sum(map(lambda x:x*x,map(int,input().split())))%10)

# a=[int(input()) for _ in range(9)]
# print(max(a))
# print(a.index(max(a))+1)

# for _ in range(int(input())):
#     print(sum(map(int,input().split())))

# for _ in range(int(input())):
#     m, string = input().split()
#     for s in string:
#         print(s*int(m),end="")
#     print()

# for i in range(int(input())):
#     print(i+1)

# n=int(input())
# i = None
# if n % 4 == 0:
#     if n % 100 == 0:
#         if n % 400 == 0:
#             i = True
#         else:
#             i= False
#     else:
#         i = True
# else:
#     i= False
# if i:
#     print(1)
# else:
#     print(0)

# h,m=map(int,input().split())
# if m<45:
#     if h==0:
#         h += 23
#     else:
#         h += -1

#     m = 60 -45 + m
# else:
#     m += -45

# print(h, m)

# v=list(map(int,input().split()))
# a=True
# for i,v in zip(range(1,9),v):
#     if i == v:
#         a=False
#     else:
#         break
# if not a:
#     print("ascending")
#     a = True


# for i,v in zip(reversed([i for i in range(1,9)],v):
#     if i == v:
#         a=False
#     else:
#         break

# if not a:
#     print("ascending")  
# if a:
    # print("mixed")


# print(len(set(list(map(lambda x:x%42,[int(input()) for _ in range(10)])))))

# n = int(input())
# if 100>=n>=90:
#     print("A")
# elif n>=80:
#     print("B")
# elif n>=70:
#     print("C")
# elif n>=60:
#     print("D")
# else:
#     print("F")

# print("""\    /\\
#  )  ( ')
# (  /  )
#  \(__)|""")

# print('''|\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\\__|''')
input()
s = 0
for i in input():
    s += int(i)
print(s)