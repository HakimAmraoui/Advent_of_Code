import os
import numpy as np

file_path = os.path.join("Inputs/Day_3/input.txt")
ans = 0

### First part

# with open(file_path) as file:

#     for line in file.readlines():
#         double = []
#         left_part = line[:len(line)//2]
#         right_part = line[len(line)//2:]
#         for l in left_part:
#             if l in right_part and l not in double:
#                 double.append(l)
#                 if ('a' <= l <= 'z'):
#                     ans += ord(l) - ord('a') + 1
#                 else:
#                     ans += ord(l) - ord('\'')                          # must redraw 38 wish is the number for ' character 

    
# print(ans)


### Second part
with open(file_path) as file:
    file = file.readlines()
    for i in range(0, len(file) // 3):
        for c in file[3 * i]:
            if c in file[3 * i + 1] and c in file[3 * i + 2]:
                if 'a' <= c <= 'z':
                    ans += ord(c) - ord('a') + 1
                else :
                    ans += ord(c) - ord('\'') + 1
                break
print(ans)