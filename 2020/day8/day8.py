import re, sys

data = open('day8Input.txt', 'r').read()
data = data.split('\n')

regex = r'(?P<instruction>\S+)\s+(?P<op>[-|+])(?P<value>\d+)'

acc = 0
ind = 0

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

    if instruction == 'nop':
        ind += 1
    elif instruction == 'acc':
        if op == '+':
            acc += int(value)
        else:
            acc -= int(value)
        ind += 1
    else:
        if op == '+':
            ind += int(value)
        else:
            ind -= int(value)

print(acc)