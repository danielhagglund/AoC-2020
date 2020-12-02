passwordpolicylist = []
correctpasswords = 0
input_data = open("./Day2/rules.txt").read().splitlines()

for line in input_data:
    passwordpolicylist.append(line.replace(":", "").split(" "))

for entry in passwordpolicylist:
    occurs = entry[0].split("-")
    min_occur = int(occurs[0])
    max_occur = int(occurs[1])
    actual_occurence = entry[2].count(entry[1])
    if actual_occurence >= min_occur and actual_occurence <= max_occur:
        correctpasswords += 1

print(correctpasswords)
