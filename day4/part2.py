count = 0
letters = []

def isCenter(row, col, char):
    if (col - 1 >= 0) and (col + 1 < len(letters[row])) and (row - 1 >= 0) and (row + 1 < len(letters)):
        if (letters[row - 1][col - 1] == char) and (letters[row + 1][col - 1] == char):
            return True
        if (letters[row + 1][col + 1] == char) and (letters[row - 1][col + 1] == char):
            return True
    return False

def checkForXedMases(row, col):
    global count
    if isCenter(row, col):
        count += 1

with open("input.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        chars = []
        for char in line:
            chars.append(char.lower())
        letters.append(chars)

for i in range(0, len(letters)):
    for j in range(0, len(letters[i])):
        if (letters[i][j] == "a"):
            checkForXedMases(i, j)
print(count)