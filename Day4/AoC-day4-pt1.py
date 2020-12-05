import re


def is_valid_passport(passport_candidate):
    valid_pid = re.search(r"pid:", passport_candidate) is not None
    valid_hgt = re.search(r"hgt:", passport_candidate) is not None
    valid_iyr = re.search(r"iyr:", passport_candidate) is not None
    valid_byr = re.search(r"byr:", passport_candidate) is not None
    valid_eyr = re.search(r"eyr:", passport_candidate) is not None
    valid_ecl = re.search(r"ecl:", passport_candidate) is not None
    valid_hcl = re.search(r"hcl:", passport_candidate) is not None

    return valid_pid and valid_hgt and valid_iyr and valid_ecl and valid_byr and valid_eyr and valid_hcl


passports = []
valid_passports = 0
input_data = open("./Day4/passports.txt").read().splitlines()

for passport in input_data:
    passports.append(passport)

row = 0

while row < len(passports)-1:
    passport = ""

    while row <= len(passports)-1 and len(passports[row]) != 0:
        passport += passports[row] + " "
        row += 1

    row += 1

    if is_valid_passport(passport):
        valid_passports += 1

print(valid_passports)
