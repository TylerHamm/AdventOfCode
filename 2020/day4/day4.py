import re

def main(data):
    '''
    Takes in the passports and validates if they have 
    all 8 keys (but cid is optional)
    return valid passports
    '''

    regex_list = {
        'eyr': r'eyr:(202[0-9]|2030)',
        'iyr': r'iyr:(201[0-9]|2020)',
        'byr': r'byr:(19[2-9][0-9]|200[1-2])',
        'ecl': r'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
        'pid': r'pid:[0-9]{9}',
        'hcl': r'hcl:#[0-9a-f]{6}',
        'hgt': r'hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)',
        # 'cid': 'cid:(?P<cid>\S+)(\s+)?',
    }
    count = 0

    data_lines = re.split('\n\n', data)

    for lines in data_lines:

        failure = False
        for key, regex in regex_list.items():
            regex_res = re.search(regex, lines)

            if not regex_res:
                failure = True
                break

        if not failure:
            count += 1

    return count

data_good = '''
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
'''

data_bad = '''
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
'''

data = open('day5Input.txt', 'r').read()
data = data.split()

value = main(data)
print(value)