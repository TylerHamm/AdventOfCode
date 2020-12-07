# Open data and split by empty lines
data = open('day6Input.txt', 'r').read()
data = data.split('\n\n')

print("## Part 1 ##")

total_count = 0
for group in data:

    curr_dict = {}
    curr_count = 0

    # put all lines on 1 line and strip
    group = group.replace('\n', '').strip()
    for char in group:
        if char not in curr_dict:
            curr_dict[char] = 1
            curr_count += 1

    total_count += curr_count

print(total_count)
print('')
print("## Part 1 Solution 2##")
# For this solution i wanted to avoid dictionaries
# I also know what part 2 is aiming for, so i will avoid
# putting it all on 1 line. Even though this is probably not
# the solution I would go for

total_count = 0
for group in data:

    char_array = [None] * 26
    group_split = group.split()

    for line in group_split:
        for char in line:
            index = ord(char) - ord('a')
            char_array[index] = 1
            
    total_count += char_array.count(1)
    
print(total_count)
print('')
print("## Part 2 ##")
# Using dictionary for part 2

total_count = 0
for group in data:

    curr_dict = {}
    curr_count = 0

    # Count lines in group
    group_size = group.count('\n') + 1

    # put all lines on 1 line and strip
    group = group.replace('\n', '').strip()

    for char in group:
        if char not in curr_dict:
            curr_dict[char] = 1
        elif char in curr_dict:
            curr_dict[char] += 1

    for k, v in curr_dict.items():
        if v == group_size:
            curr_count += 1

    total_count += curr_count

print(total_count)