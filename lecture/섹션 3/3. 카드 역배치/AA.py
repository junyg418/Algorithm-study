import sys
sys.stdin = open('input.txt')
lists = list(range(1,21))
for _ in range(10):
    a, b = map(int, input().split())
    aidx = lists.index(a)
    bidx = lists.index(b)

    front = lists[:aidx]
    back = lists[bidx+1:]
    val = lists[aidx:bidx+1]
    del lists[aidx:bidx+1]
    val.reverse()
    lists = front + val + back
print(lists)