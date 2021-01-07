import re

# advent of code day4 2020

f = open('input')
data = f.read().split("\n\n")


valid = 0
dicts = []
for p in data:
    d = {}
    for x in p.split():
        # print(x)
        k, v = x.split(':')
        d[k] = v
    dicts.append(d)
    # print("---------------------")

# solve part 1
for d in dicts:
    if len(d) == 8:
        valid += 1
    elif len(d) == 7 and not 'cid' in d.keys():
        valid += 1
print(f"Part 1: Number of valid passports: {valid}")



# solve part 2
def height_valid(h):
    if h[-2:] == 'in':
        if int(h[:-2]) >= 59 and int(h[:-2]) <= 76:
            return True
        else:
            return False
    elif h[-2:] == 'cm':
        if int(h[:-2]) >= 150 and int(h[:-2]) <= 193:
            return True
        else:
            return False

def pid_valid(x):
    if re.search('\d{9}', x) and len(x) == 9:
        return True
    return False

def hair_valid(x):
    if re.search('#(\d|[a-f]){6}', x) and len(x) == 7:
        return True
    return False

def eye_valid(x):
    if re.search('amb|blu|brn|gry|grn|hzl|oth', x):
        return True
    return False
    

def d_valid(d):
    return (
        int(d['byr']) >= 1920 and int(d['byr']) <= 2002
        and int(d['iyr']) >= 2010 and int(d['iyr']) <= 2020
        and int(d['eyr']) >= 2020 and int(d['eyr']) <= 2030
        and height_valid(d['hgt'])
        and pid_valid(d['pid'])
        and eye_valid(d['ecl'])
        and hair_valid(d['hcl'])
    )

valid = 0
for d in dicts:
    if len(d) == 8:
        if d_valid(d):
            valid += 1
    elif len(d) == 7 and not 'cid' in d.keys():
        if d_valid(d):
            valid += 1
print(f"Part 2: Number of valid passports: {valid}")
