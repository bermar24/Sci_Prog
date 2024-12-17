
def NewMat():
    Row = int(input("Enter the number of rows:"))
    Column = int(input("Enter the number of columns:"))

    # Initialize matrix
    matrix = []
    print("Enter the entries row wise:")

    # For user input
    # A for loop for row entries
    for row in range(Row):
        a = []
        # A for loop for column entries
        for column in range(Column):
            a.append(int(input()))
        matrix.append(a)
    return matrix

# For printing the matrix
def PrintMatrix(matrix):
    row = len(matrix)
    column = len(matrix[0])
    for row in range(row):
        for column in range(column):
            print(matrix[row][column], end=" ")
        print()

# Asigning Matrix A and B
MatA = NewMat()
PrintMatrix(MatA)
MatB = NewMat()
PrintMatrix(MatB)
