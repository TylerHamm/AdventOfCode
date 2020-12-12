import re

data = open('day7InputSimple.txt', 'r').read()
data = data.split('\n')

shiny_dict = {}

count = 0
for line in data:
    regex = r'(?P<outer-bag>)'
    regex_result = re.search(regex, line)

print(count)