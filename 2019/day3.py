with open("D:\Documents\AdventOfCode\Day_3\Input.txt") as file:
    map = file.readlines()
    map = [line.strip() for line in map]


def firstTask():
    treesCount = 0
    row, col = 0, 0

    while row + 1 < len(map):
        row += 1
        col += 3

        space = map[row][col % len(map[row])]
        if space == '#':
            treesCount += 1

    return treesCount


def secondTask(x, y):
    treesCount = 0
    row, col = 0, 0

    while row + y < len(map):
        row += y
        col += x

        space = map[row][col % len(map[row])]
        if space == '#':
            treesCount += 1

    return treesCount


print(firstTask())
print("Right 1, down 1 : ", secondTask(1, 1))
print("Right 3, down 1 : ", secondTask(3, 1))
print("Right 5, down 1 : ", secondTask(5, 1))
print("Right 7, down 1 : ", secondTask(7, 1))
print("Right 1, down 2 : ", secondTask(1, 2))

print("The result for the second task is : ",
      secondTask(1, 1) * secondTask(3, 1) * secondTask(5, 1) * secondTask(7, 1) * secondTask(1, 2))
