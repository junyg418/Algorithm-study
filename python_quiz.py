def myfct(input_list):
    result = []
    data = len(input_list[0]) -1
    for value in input_list:
        result.append(value[data])
        data += -1
    return result

def myfct(lt):
    list1 = []
    data = len(lt[0])
    for i in lt:
        list1.append(i[data-1])
        data = data - 1
    return list1

lt1 = [
    [1,2,3,1],
    [4,5,6,4],
    [7,8,9,7]
]

# lt2 = [
#     []
# ]

print(myfct(lt1))