import time

data = open('day1Input.txt', 'r').read()
data = data.split('\n')

target = 2020
d = {}
value = 0

## Solution 1
initial_time = time.perf_counter()
for i in range(0, len(data)):
    line = int(data[i])
    for second in data[i:]:
        if line + int(second) == target:
            value = line*int(second)
            break
final_time = time.perf_counter() - initial_time
print(value)
print(final_time)
## Solution 2

initial_time = time.perf_counter()
for line in data:
    curr = int(line)
    d[curr]=curr
    partner = target - curr
    if partner in d:
        value = curr*partner
final_time_2 = time.perf_counter() - initial_time
print(value)
print(final_time_2)

print('### Part 2 ###')
initial_time = time.perf_counter()
for i in range(0, len(data)):
    line = int(data[i])
    for second in data[i:]:
        curr = int(second)
        curr_target = target - line
        d[curr]=curr
        partner = curr_target - curr
        if partner in d:
            value = curr*partner*line

final_time_3 = time.perf_counter() - initial_time
print(value)
print(final_time_3)

## Solution 2

initial_time = time.perf_counter()

for line in data:
    d[line] = line

for i in range(0, len(data)):
    line = int(data[i])
    for j in range(i+1, len(data)):
        second = int(data[j])
        partner = target - line - second
        if partner in d:
            value = line*second*d[partner]

final_time_4 = time.perf_counter() - initial_time
print(value)
print(final_time_4)