import os

file_path = os.path.join('Inputs/Day_4/input.txt')
ans_1 = 0
ans_2 = 0

### First part
with open(file_path) as file:
    for line in file:
        one, two = line.split(',')
        s1, e1 = one.split('-')
        s2, e2 = two.split('-')
        s1, e1, s2, e2 = [int(x) for x in [s1, e1, s2, e2]]
        if s1 <= s2 and e2  <= e1 or s2 <= s1 and e1  <= e2:
            ans_1 += 1
        if not (e1 < s2 or e2 < s1):
            ans_2 += 1
print(ans_1)
print(ans_2)