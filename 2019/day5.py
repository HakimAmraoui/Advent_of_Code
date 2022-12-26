with open(".\Inputs\Day_5\Input.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]

seats = []


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def Row(string):
    min, max = 0, 127
    # We devide the string until there is only one row left
    while min != max:
        if (string[0] == 'F'):
            max = int((max + min) / 2)
            string = string[1:]
        else:
            min = int((min + max + 1) / 2)
            string = string[1:]
    return min


def Column(string):
    # We devide the string until there is only one column left
    min, max = 0, 7
    while min != max:
        if (string[0] == 'L'):
            max = int((max + min) / 2)
            string = string[1:]
        else:
            min = int((min + max + 1) / 2)
            string = string[1:]
    return min


# def CalculateSeatID(r, c):
#     seatId = r * 8 + c
#     seats.append(seatId)

for lines in data:
    row, column = 0, 0
    row = Row(lines[0:7])
    column = Column(lines[7:])
    seatID = (row * 8) + column
    # We add this seat to the list
    seats.append(seatID)

mergeSort(seats)
print('The result for the first task is : ', seats[len(seats) - 1])

def ResearchMissingSeat(seats):
    for seat in range(0, 935):
        # If a seat is not in the list
        if (seat not in seats):
            # if the seat has a previous and a next seat, it's the missing one
            if((seat+1) in seats and (seat-1) in seats):
                return seat


print('The result for the second task is : ', ResearchMissingSeat(seats))