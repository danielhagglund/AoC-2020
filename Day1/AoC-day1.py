input_list = []

input_data = open("./Day1/input.txt").read().splitlines()

for x in input_data:
    input_list.append(int(x))

for a in input_list:
    for b in input_list:
        for c in input_list:
            if (a+b+c) == 2020:
                print(a)
                print(b)
                print(c)
                print(a*b*c)
                break
