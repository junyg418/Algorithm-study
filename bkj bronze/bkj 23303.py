input_data = input()

flag = True

for idx, value in enumerate(input_data):
    if value.lower() == "d":
        if idx != len(input_data)-1:
            if  input_data[idx+1] == "2":
                flag = False
                print("D2")
                break

if flag:
    print("unrated")