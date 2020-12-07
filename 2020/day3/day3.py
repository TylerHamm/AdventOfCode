
def main(data, right, down):
    '''
    Takes in the given data for the problem set
    returns tree count
    '''

    right_index = 1

    right_movement = right
    down_movement = down

    down_count = 0
    tree_count = 0    

    # Loop through data
    for line_index in range(0, len(data_array), down_movement):

        line = data_array[line_index]

        # check position - 1 (take into consideration index starts at 0)
        value = line[right_index - 1]

        if value == '#':
            tree_count += 1

        new_line = line[:right_index-1] + 'X' + line[right_index-1:]
        data_array[down_count] = new_line
        
        # add _movement to _index
        right_index += right_movement

        # if right > 10, take mod
        if right_index > len(line):
            right_index %= len(line)

        down_count += 1

    # for line in data_array:
    #     print(line)

    return(tree_count)

data = open('day5Input.txt', 'r').read()
data = data.split()

right_array = [1,3,5,7,1]
down_array = [1,1,1,1,2]

trees_hit = 1

for i in range(0,5):
    trees_hit *= main(data, right_array[i], down_array[i])

print(trees_hit)