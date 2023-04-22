def int_sort(iterator):
    max_val = max(iterator)
    cnt_list = [0 for _ in range(max_val+1)]
    for val in iterator:
        cnt_list[val] += 1
    result_val = [idx for idx, val in enumerate(cnt_list) for _ in range(val)]
    return result_val

llst = [1,6,6,2,4]
print(int_sort(llst))