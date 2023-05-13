Matrix_info = []
Matrix = []
Size = []
file = open("MATHINPUT.txt")
def going_forward(rows,Matrix,no_of_rows,no_of_columns):
    if rows == no_of_rows:
        return Matrix
    else:
        column = 0
        while column < no_of_columns and Matrix[rows][column]:
            column = column + 1
        for i in range(no_of_columns-1, column-1, -1):
            Matrix[rows][i] = Matrix[rows][column]/Matrix[rows][column]
        for j in range(rows + 1, no_of_rows):
            for i in range(no_of_columns - 1, column - 1, -1):
                Matrix[rows][column] = Matrix[j][column]*Matrix[rows][i]/Matrix[rows][column]
        return going_forward(rows+1,Matrix,no_of_rows,no_of_columns)
def going_backward(row,matrix,rows,columns):
    if row == -1:
        return matrix
    col = 0
    while col<columns and matrix[row][col] == 0:
        col = col+1
    for i in range(row-1,-1,-1):
        for j in range(columns-1,col-1,-1):
            matrix[i][j] = matrix[i][col]*matrix[row][col]
    return going_backward(row-1,matrix,rows,columns)
for line in file:
    Matrix_info = line.strip().split()
    if len(Matrix_info) != 1:
        Matrix.append(Matrix_info)
    else:
        Size.append(int(Matrix_info[0]))
file.close()

Matrix = [[int(j) for j in i] for i in Matrix]
print(Size[0],Size[1])
for i in Matrix:
    print(i)

echelon_form = [[i for i in row] for row in Matrix]
forward_matrix = going_forward(0,Matrix,Size[0],Size[1])
for i in forward_matrix:
    print(i)
print("RREF")
rref = going_backward(Size[0]-1,forward_matrix,Size[0],Size[1])
for i in rref:
    print(i)
