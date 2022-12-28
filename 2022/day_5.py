import os

file_path = os.path.join('Inputs/Day_5/input.txt')
pile = [[] for i in range(9)]

### First part

# with open(file_path) as file:
#     for line in file:
#         if line[0] == '[':
#             for i in range(9):
#                 if line[i * 4 + 1] != ' ':
#                     pile[i].insert(0, line[i * 4 + 1])
#         elif line[0] == 'm':
#             line = line.split(' ')
#             n, s, e = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
#             for i in range(n):
#                 pile[e].append(pile[s].pop())
# s = ""
# for i in range(len(pile)):
#     s += pile[i].pop()
# print(s)        

### Second part

with open(file_path) as file:
    for line in file:
        if line[0] == '[':
            for i in range(9):
                if line[i * 4 + 1] != ' ':
                    pile[i].insert(0, line[i * 4 + 1])
        elif line[0] == 'm':
            line = line.split(' ')
            n, s, e = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
            to_move = pile[s] [len(pile[s]) - n:]
            for x in to_move:
                pile[e].append(x)
            for i in range(n):
                pile[s].pop()
s = ""
for i in range(len(pile)):
    s += pile[i].pop()
print(s)        


# a = ['1', '2', '3']
# # b = a.pop(3)
# print(a[len(a) - 2:])