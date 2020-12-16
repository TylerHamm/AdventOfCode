import re, sys

data = open('day8Input.txt', 'r').read()
data = data.split('\n')

regex = r'(?P<instruction>\S+)\s+(?P<op>[-|+])(?P<value>\d+)'

acc = 0
ind = 0
final_jmp_ind = 0
changed = False

jmp_arr = [False] * len(data)
jmp_arr_all = [False] * len(data)

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
    line_raw = data[i]
    line = re.search(regex, line_raw)

    instruction = line.group('instruction')
    op = line.group('op')
    value = int(line.group('value'))

    if instruction == 'jmp':
        if op == '+':
            # if value + i > 600:
            #     print(line)
            #     print(value)
            #     print(i)
            #     print(final_jmp_ind)
            #     print(value + i)
            if value + i > final_jmp_ind:
                jmp_arr[i] = True
        jmp_arr_all[i] = True

for i in range(len(jmp_arr)):
    if jmp_arr[i]:
        print(i)
        print(data[i])

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

    # Validate if you change a nop to a jump. if it will
    # Take you to a jump that will surpase the last jump
    # AKA, the jmp_arr
    if instruction == 'nop':
        if op == '+':
            curr_pointer = ind - int(value)
            while(True):
                print(curr_pointer)
                if jmp_arr[curr_pointer]:
                    changed = True
                    instruction = 'jmp'
                curr_pointer += 1
                if jmp_arr_all[curr_pointer] and \
                    not jmp_arr[curr_pointer]:
                    break
        elif op == '-':
            curr_pointer = ind - int(value)
            while(True):
                print(curr_pointer)
                if jmp_arr[curr_pointer]:
                    changed = True
                    instruction = 'jmp'
                curr_pointer += 1
                if jmp_arr_all[curr_pointer] and \
                    not jmp_arr[curr_pointer]:
                    break

    #     print(ind)
    #     print(line_raw)
    #     print(ind + int(value))

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