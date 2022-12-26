with open(".\Inputs\Day_7\Input.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

rules = {}

for lines in data:
    line = lines.split(' ')
    rules.update({line[0]: line[4:]})

print(rules['dark'])