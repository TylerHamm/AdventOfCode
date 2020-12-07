data = open('day5Input.txt', 'r').read()
data = data.split()
# For ease use 128 then subtract 1 later
max_val = 0

id_list = []

# Loop through data
for line in data:
    r_p_1 = 0
    r_p_2 = 128

    c_p_1 = 0
    c_p_2 = 8

    row = -1
    column = -1
    # Loop through string
    for char in line[:6]:
        if char == 'F':
            r_p_2 = int(r_p_2 - ((r_p_2 - r_p_1) / 2))
        elif char == 'B':
            r_p_1 = int(r_p_1 + ((r_p_2 - r_p_1) / 2))

    # Compensate for easier math earlier
    r_p_2 -= 1

    # Check last number
    char = line[6]
    if char == 'F':
        row = r_p_1
    else:
        row = r_p_2
    
    for char in line[7:9]:
        if char == "L":
            c_p_2 = int(c_p_2 - ((c_p_2 - c_p_1) / 2))
        elif char == 'R':
            c_p_1 = int(c_p_1 + ((c_p_2 - c_p_1) / 2))
    
    c_p_2 -= 1

    char = line[9]
    if char == "L":
        column = c_p_1
    else:
        column = c_p_2

    value = row * 8 + column

    if value > max_val:
        max_val = int(value)

    id_list.append(value)

id_list = sorted(id_list)
ur_seat = -1

for i in range(0,len(id_list)-2):
    if (id_list[i]+2) == id_list[i+1]:
        ur_seat = id_list[i]+1

print(ur_seat)
print(max_val)