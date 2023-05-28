while True:
    input_data = input()
    if input_data == "0 0 0":
        break
    input_data = list(map(int, input_data.split()))
    bit = max(input_data)
    bit_idx = input_data.index(bit)
    input_data.pop(bit_idx)
    x, y = input_data
    if x**2 + y**2 == bit**2:
        print("right")
    else:
        print("wrong")