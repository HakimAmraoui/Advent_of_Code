import array

file = open("D:\Documents\AdventOfCode\Day_2\Input.txt", "r")

myList = []

for lines in file:
    line = lines.split("\n")
    myList.append(line[0])

file.close()


def firstTask():
    c = 0

    for lines in myList:

        # We split the line from the ":", with on the left the rules and on the right the psw

        line = lines.split(":")
        rules = line[0]
        psw = line[1]

        # We split the rule from the space, with on the left the numbers and on the left the letter
        rule = rules.split(" ")
        ints = rule[0].split("-")
        intMin = int(ints[0])
        intMax = int(ints[1])

        # We isolate the letter
        letter = rule[1]

        repetition = 0

        # We compare each letter of the psw with the good one if it is the same
        for l in psw:
            if l == letter:
                repetition += 1

        if (intMin <= repetition and repetition <= intMax):
            c = c + 1

    return c


def secondTask():
    c = 0

    for lines in myList:

        # We split the line from the ":", with on the left the rules and on the right the psw

        line = lines.split(":")
        rules = line[0]
        psw = line[1]

        # We split the rule from the space, with on the left the numbers and on the left the letter
        rule = rules.split(" ")
        ints = rule[0].split("-")
        intMin = int(ints[0])
        intMax = int(ints[1])

        # We isolate the letter
        letter = rule[1]



        if ((psw[intMin] == letter) ^ (psw[intMax] == letter)):
            c = c + 1

    return c


print("The solution for the first task is : ", firstTask())
print("The solution for the second task is : ", secondTask())

print(int(0o0000003))
