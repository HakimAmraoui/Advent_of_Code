import os
import numpy as np

file_path = os.path.join("Inputs/Day_1/input.txt")

c = 0
elves_calories = []

with open(file_path, "r") as file:
    for line in file:
        if line != "\n":
            c += int(line)
        else :
            elves_calories.append(c)
            c = 0

print(f'The Elf carring the most calories is {np.argmax(elves_calories)} with {elves_calories[np.argmax(elves_calories)]} calories.')

t = 0
for i in np.argsort(elves_calories)[-3:][::-1]:
    t += elves_calories[i]
print(f'The top three are : {np.argsort(elves_calories)[-3:][::-1]} with a total of {t} calories.')
