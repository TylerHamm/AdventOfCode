import re, sys

data = open('day8Input.txt', 'r').read()
data = data.split('\n')

regex = r'(?P<instruction>\S+)\s+(?P<op>[-|+])(?P<value>\d+)'

acc = 0
ind = 0
final_jmp_ind = 0
changed = False

nop_arr = [False] * len(data)

# Debug
max_ind = 0

# Find final jump ind
for i in reversed(range(len(data))):
    line_raw = data[i]
    line = re.search(regex, line_raw)

    if line.group('instruction') == 'jmp' and \
        line.group('op') == '-':
        final_jmp_ind = i
        break

for i in range(len(data)):
    if line.group('instruction') == 'jmp':
        if line.group('op') == '+':
            if line.group('value') + i > final_jump_ind:
                nop_arr[i] = True



while(ind < len(data)):
    line_raw = data[ind]
    line = re.search(regex, line_raw)

    # As i replace the line with null, regex will fail
    # This does assume good input but that should be fine
    # For this purpose
    if not line:
        break

    # Delete line
    data[ind] = ''

    instruction = line.group('instruction')
    op = line.group('op')
    value = line.group('value')

    if ind == final_jmp_ind:
        instruction = 'nop'
        changed = True

    if instruction == 'nop':
        if op == '+' and not changed:
            if int(value) + ind > final_jmp_ind:
                changed = True
                instruction = 'jmp'
            else:
                ind += 1
        else:
            ind += 1
    if instruction == 'acc':
        if op == '+':
            acc += int(value)
        else:
            acc -= int(value)
        ind += 1
    if instruction == 'jmp':
        if op == '+':
            ind += int(value)
        else:
            ind -= int(value)
    
    if ind > max_ind:
        max_ind = ind

print(max_ind)
print(ind)
print(final_jmp_ind)
print(changed)
print(acc)