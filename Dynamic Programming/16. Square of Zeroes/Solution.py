# O(n^4) time | O(n^3) space - where n is the height and width of the matrix
def squareOfZeroes(matrix):
    n  = len(matrix)
    for topRow in range(n):
        for leftCol in range(n):
            squareLength = 2
            while squareLength <= n - leftCol and squareLength <= n - topRow:
                bottomRow = topRow + squareLength - 1
                rightCol = leftCol + squareLength - 1
                if isSquareOfZeroes(matrix, topRow, leftCol, bottomRow, rightCol):
                    return True
                squareLength += 1
    return False

# r1 is the top row, c1 is the left column
# #r2 is the bottom row, c2 is the right column
def isSquareOfZeroes(matrix, r1, c1, r2, c2):
    for row in range(r1, r2 + 1):
        if matrix[row][c1] != 0 or matrix[row][c2] != 0:
            return False
    for col in range(c1, c2 + 1):
        if matrix[r1][col] != 0 or matrix[r2][col] != 0:
            return False
    return True
