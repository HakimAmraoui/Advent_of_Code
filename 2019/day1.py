import array


file = open("D:\Documents\AdventOfCode\Day_1\Input.txt", "r")

myList = []


for lines in file:
    line = lines.split("\n")
    myList.append(int(line[0]))

file.close()

def firstTask():
    for i in myList:

        for j in myList:

            if i + j == 2020:

                return i * j

def secondTask():
    for i in myList:

        for j in myList:

            for k in myList:
                if i + j + k == 2020:

                    return i * j * k




print("The result for the first task is : ",firstTask())
print("The result for the second task is : ", secondTask())

