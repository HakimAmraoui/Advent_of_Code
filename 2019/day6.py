with open(".\Inputs\Day_6\Input.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

### PART 1

def get_unique_answer(response) :
    question = []
    for char in response:
        if char not in question:
            question.append(char)
    return len(question)

currentResponses = ''
sum = 0

for line in data:
    if line != '':
        currentResponses += line
    else:
        sum += get_unique_answer(currentResponses)
        currentResponses = ''

sum += get_unique_answer(currentResponses)

print('The result for the first task is : ', sum)


### PART 2

def get_unique_answer_all(responses):
    questions = []
    isInAllResponses = True

    for char in responses[0]:
        isInAllResponses = True
        for line in responses:
            if char not in line:
                isInAllResponses = False
        if isInAllResponses and char not in questions:
            questions.append(char)

    return len(questions)

sum = 0
currentResponses = []

for line in data:
    if line != '':
        currentResponses.append(line)
    else:
        sum += get_unique_answer_all(currentResponses)
        currentResponses.clear()

sum += get_unique_answer_all(currentResponses)

print('The result for the second task is : ', sum)
