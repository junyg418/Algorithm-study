while True:
    input_data = input()
    if input_data == "0":
        break
    if len(input_data) %2 == 0:
        len_data = len(input_data)//2
        for idx in range(len_data):
            back_data = -idx -1
            if input_data[idx] == input_data[back_data]:
                continue
            else:
                break
        else:
            print("yes")
            continue
        print("no")
    else:
        len_data = len(input_data)//2
        for idx in range(len_data):
            back_data = -idx -1
            if input_data[idx] == input_data[back_data]:
                continue
            else:
                break
        else:
            print("yes")
            continue
        print("no")