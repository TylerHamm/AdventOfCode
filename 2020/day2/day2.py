import re
data = open('day2Input.txt', 'r').read()
data = data.split('\n')

regex = r'(?P<lower>\d+)-(?P<upper>\d+)\s+(?P<target>\w+):\s+(?P<password>\w+)'

valid = 0
for line in data:
    re_result = re.search(regex, line)

    if not re_result:
        continue

    lower_limit = int(re_result.group('lower'))
    upper_limit = int(re_result.group('upper'))
    target_letter = re_result.group('target')
    password = re_result.group('password')

    count = 0
    for char in password:
        if char == target_letter:

            count += 1
    
    if count >= lower_limit and count <= upper_limit:
        valid += 1

print(valid)

print('#### PART 2 ####')
## Part 2

valid = 0
for line in data:
    re_result = re.search(regex, line)

    if not re_result:
        continue

    lower_limit = int(re_result.group('lower'))
    upper_limit = int(re_result.group('upper'))
    target_letter = re_result.group('target')
    password = re_result.group('password')

    count = 0
    lower_char = password[lower_limit-1]
    upper_char = password[upper_limit-1]

    if lower_char == target_letter:
        count += 1
    if upper_char == target_letter:
        count += 1

    if count == 1:
        valid += 1

print(valid)