import numpy as np
import os

file_path = os.path.join("Inputs/Day_2/input.txt")
score = []
score_2 = []

def game(a, b):
    if (a == "A"):
        if (b == "X"):
            return 1 + 3
        elif (b == "Y"):
            return 2 + 6
        elif (b == "Z"):
            return 3 + 0
    elif (a == "B"):
        if (b == "X"):
            return 1 + 0
        elif (b == "Y"):
            return 2 + 3
        elif (b == "Z"):
            return 3 + 6
    elif (a == "C"):
        if (b == "X"):
            return 1 + 6
        elif (b == "Y"):
            return 2 + 0
        elif (b == "Z"):
            return 3 + 3

def game_2(a, b):
    if (a == "A"):
        if (b == "X"):
            return 3
        elif (b == "Y"):
            return 1 + 3
        elif (b == "Z"):
            return 2 + 6
    elif (a == "B"):
        if (b == "X"):
            return 1 + 0
        elif (b == "Y"):
            return 2 + 3
        elif (b == "Z"):
            return 3 + 6
    elif (a == "C"):
        if (b == "X"):
            return 2 + 0
        elif (b == "Y"):
            return 3 + 3
        elif (b == "Z"):
            return 1 + 6

with open(file_path, "r") as file:
    for line in file:
        l = line.split()
        score.append(game(l[0], l[1]))
        score_2.append(game_2(l[0], l[1]))
    print(f'The answer of the first part is : {np.sum(score)}')
    print(f'The answer of the second part is : {np.sum(score_2)}')



