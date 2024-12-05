count = 0
letters = []

def checkForward(row, col):
    global count
    if col + 3 < len(letters[row]):
        if (letters[row][col] == "x" and letters[row][col + 1] == "m" and letters[row][col + 2] == "a" and letters[row][col + 3] == "s") or (letters[row][col] == "s" and letters[row][col + 1] == "a" and letters[row][col + 2] == "m" and letters[row][col + 3] == "x"):
            count += 1
def checkDown(row, col):
    global count
    if row + 3 < len(letters):
        if (letters[row][col] == "x" and letters[row + 1][col] == "m" and letters[row + 2][col] == "a" and letters[row + 3][col] == "s") or (letters[row][col] == "s" and letters[row + 1][col] == "a" and letters[row + 2][col] == "m" and letters[row + 3][col] == "x"):
            count += 1
def checkLeftDiagonal(row, col):
    global count
    if row + 3 < len(letters) and col - 3 >= 0:
        if (letters[row][col] == "x" and letters[row + 1][col - 1] == "m" and letters[row + 2][col - 2] == "a" and letters[row + 3][col - 3] == "s") or (letters[row][col] == "s" and letters[row + 1][col - 1] == "a" and letters[row + 2][col - 2] == "m" and letters[row + 3][col - 3] == "x"):
            count += 1
def checkRightDiagonal(row, col):
    global count
    if row + 3 < len(letters) and col + 3 < len(letters[row]):
        if (letters[row][col] == "x" and letters[row + 1][col + 1] == "m" and letters[row + 2][col + 2] == "a" and letters[row + 3][col + 3] == "s") or (letters[row][col] == "s" and letters[row + 1][col + 1] == "a" and letters[row + 2][col + 2] == "m" and letters[row + 3][col + 3] == "x"):
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
        checkForward(i, j)
        checkDown(i, j)
        checkLeftDiagonal(i, j)
        checkRightDiagonal(i, j)

print(count)