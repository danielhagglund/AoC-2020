import re


def is_valid_byr(passport_candidate):
    valid = False
    byr_match = re.search(r"byr:\d{4}(\s|$)", passport_candidate)
    if byr_match is not None:
        year = int(byr_match.group().strip()[4:])
        if year >= 1920 and year <= 2002:
            valid = True
    return valid


def is_valid_iyr(passport_candidate):
    valid = False
    iyr_match = re.search(r"iyr:\d{4}(\s|$)", passport_candidate)
    if iyr_match is not None:
        year = int(iyr_match.group().strip()[4:])
        if year >= 2010 and year <= 2020:
            valid = True
    return valid


def is_valid_eyr(passport_candidate):
    valid = False
    eyr_match = re.search(r"eyr:\d{4}(\s|$)", passport_candidate)
    if eyr_match is not None:
        year = int(eyr_match.group().strip()[4:])
        if year >= 2020 and year <= 2030:
            valid = True
    return valid


def is_valid_hgt(passport_candidate):
    valid = False
    hgt_match = re.search(
        r"hgt:((\d{2}in)|(\d{3}cm))(\s|$)", passport_candidate)
    if hgt_match is not None:
        unit = hgt_match.group().strip()[-2:]
        if unit == "cm":
            length = int(hgt_match.group().strip()[-5:-2])
            if length >= 150 and length <= 193:
                valid = True
        if unit == "in":
            length = int(hgt_match.group().strip()[-4:-2])
            if length >= 59 and length <= 76:
                valid = True
    return valid


def is_valid_passport(passport_candidate):
    valid_pid = re.search(r"pid:\d{9}(\s|$)", passport_candidate) is not None
    valid_hgt = is_valid_hgt(passport_candidate)
    valid_iyr = is_valid_iyr(passport_candidate)
    valid_byr = is_valid_byr(passport_candidate)
    valid_eyr = is_valid_eyr(passport_candidate)
    valid_ecl = re.search(
        r"ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)", passport_candidate) is not None
    valid_hcl = re.search(
        r"hcl:#([a-f]|\d){6}(\s|$)", passport_candidate) is not None

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
