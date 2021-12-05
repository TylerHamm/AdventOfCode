import re, sys

data = open('day8Input.txt', 'r').read()
data = data.split('\n')

regex = r'(?P<instruction>\S+)\s+(?P<op>[-|+])(?P<value>\d+)'

nop_list = []
jmp_list = []

acc = 0
max_ind = 0

def main_while(change_index):
 
    acc_curr = 0
    ind = 0
    global max_ind

    
    data_curr = data.copy()

    while(ind < len(data)):
        line_raw = data_curr[ind]
        line = re.search(regex, line_raw)

        # As i replace the line with null, regex will fail
        # This does assume good input but that should be fine
        # For this purpose
        if not line:
            break

        # Delete line
        data_curr[ind] = ''

        instruction = line.group('instruction')
        op = line.group('op')
        value = line.group('value')

        if ind == change_index:
            if instruction == 'nop':
                instruction = 'jmp'
            elif instruction == 'jmp':
                instruction = 'nop'

        if instruction == 'nop':
            ind += 1
        elif instruction == 'acc':
            if op == '+':
                acc_curr += int(value)
            else:
                acc_curr -= int(value)
            ind += 1
        else:
            if op == '+':
                ind += int(value)
            else:
                ind -= int(value)

    print(ind)
    print(acc_curr)
    # print(len(data))

    if ind > max_ind:
        max_ind = ind
        print("###################")
        print(max_ind)
 
    if ind >= len(data):
        return acc_curr
    else:
        return 0

for i, line in enumerate(data):
    line = re.search(regex, line)

    instruction = line.group('instruction')
    op = line.group('op')
    value = line.group('value')

    if instruction == 'jmp':
        jmp_list.append(i)
    elif instruction == 'nop':
        nop_list.append(i) 

found = False
for index in jmp_list:
    success = main_while(index)
    if success:
        acc = success
        found = True
        break

if not found:
    for index in nop_list:
        success = main_while(index)
        if success:
            acc = success
            found = True
            break

print(found)
print(acc)