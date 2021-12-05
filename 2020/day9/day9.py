data = open('day9Input.txt', 'r').read()
data = data.split('\n')

valid_nums = [None] * 25
curr_ind = 0
preamble = True
failed_num = -1

for i, line in enumerate(data):
    valid = False
    curr_num = int(line.strip())

    if curr_ind >= 25:
        preamble = False
        curr_ind = 0

    if preamble:
        valid_nums[curr_ind] = curr_num
        curr_ind += 1
        continue

    # If not preamble, make sure curr_num is valid
    for j_e, j in enumerate(valid_nums):
        target = curr_num - j
        if target < 0:
            continue
        
        for k_e, k in enumerate(valid_nums):
            # Make sure you are not using the same num
            if j_e == k_e:
                continue

            if target - k == 0:
                valid = True
                break
        
        if valid:        
            valid_nums[curr_ind] = curr_num
            curr_ind += 1
            break
    
    if not valid:
        failed_num = curr_num
        break

print(failed_num)