passwordpolicylist = []
correctpasswords = 0
input_data = open("./Day2/rules.txt").read().splitlines()

for line in input_data:
    passwordpolicylist.append(line.replace(":", "").split(" "))

for entry in passwordpolicylist:
    occurs = entry[0].split("-")
    first_occur = int(occurs[0])-1
    second_occur = int(occurs[1])-1
    occurs1 = entry[2][first_occur] == entry[1]
    occurs2 = entry[2][second_occur] == entry[1]

    if (occurs1 and not occurs2) or (occurs2 and not occurs1):
        correctpasswords += 1

print(correctpasswords)
