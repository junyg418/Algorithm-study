# import sys
# sys.stdin = open('input.txt')
n = int(input())
for i in range(n):
    st = input()
    st = st.upper()
    for k in range(len(st)//2):
        if st[k] != st[-k-1]:
            print(f"#{i+1} NO")
            break
    else:
        print(f"#{i+1} YES")