row, column = map(int, input().split())

ex1 = [["W","B","W","B","W","B","W","B"],
       ["B","W","B","W","B","W","B","W"],
       ["W","B","W","B","W","B","W","B"],
       ["B","W","B","W","B","W","B","W"],
       ["W","B","W","B","W","B","W","B"],
       ["B","W","B","W","B","W","B","W"],
       ["W","B","W","B","W","B","W","B"],
       ["B","W","B","W","B","W","B","W"]]

ex2 = [["B","W","B","W","B","W","B","W"],
       ["W","B","W","B","W","B","W","B"],
       ["B","W","B","W","B","W","B","W"],
       ["W","B","W","B","W","B","W","B"],
       ["B","W","B","W","B","W","B","W"],
       ["W","B","W","B","W","B","W","B"],
       ["B","W","B","W","B","W","B","W"],
       ["W","B","W","B","W","B","W","B"]]

input_value = [input() for _ in range(row)]

def getCount(start_pos:tuple, sample:list)->int:
    count = 0
    ro, co = start_pos
    for r in range(8):
        for c in range(8):
            if input_value[ro+r][co+c] == sample[r][c]:
                count += 1
    print(count)
    return count


result_v = []

for rr in range(row-7):
    for cc in range(column-7):
       result_v.append(min(getCount((rr, cc), ex1), getCount((rr, cc), ex2)))

print(min(result_v))