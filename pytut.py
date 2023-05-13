# TO INTERCHANGE TWO ROWS
def interchange(arr,ind_1,ind_2):
    T = arr[ind_1]
    arr[ind_1] = arr[ind_2]
    arr[ind_2] = T
    return arr
# Forward phase of RREF
def going_forward(row_no, Matrix, number_of_rows, number_of_columns):
    if row_no != number_of_rows:
        base_condition = False
    else:
        base_condition = True
    if base_condition:
        return Matrix

    column = 0

    while column < number_of_columns and Matrix[row_no][column] == 0:
        column = column + 1
    for columns in range(number_of_columns-1, column-1, -1):
        Matrix[row_no][columns] /= (Matrix[row_no][column])
    for rows in range(row_no+1, number_of_rows):
        for columns in range(number_of_columns-1, column-1, -1):
            Matrix[rows][columns]  = Matrix[rows][columns] - (Matrix[rows][column] * Matrix[row_no][columns]) # We don't require this because we already made the dividing factor one in the 21st line / Matrix[row_no][column]
    # for i in range(row_no+1, number_of_rows):
    #     for j in range(number_of_columns - 1,column - 1,-1):
    #         if abs(j) <= 0.00000000000000000000000000000001:
    #             Matrix[i][j] = 0
    # USING RECURSION AS MAM MENTIONED IN THE CLASS.
    return going_forward(row_no+1, Matrix, number_of_rows, number_of_columns)

# TO PERFORM A GIVEN ROW OPERATION WHEN THE SCALER TO BE USED IS PREDEFINED.
def row_operation(Matrix,i,scaler,j):

    a = len(Matrix[0])

    for k in range(a):
        Matrix[i][k] = Matrix[i][k] + scaler*Matrix[j][k]
    return(Matrix)
# BACKWARD PHASE
def going_backward(row_no, Matrix, number_of_rows, number_of_columns):
    if row_no != -1:
        base_condition = False
    else:
        base_condition = True
    if base_condition:
        return Matrix

    column = 0
    while column < number_of_columns and Matrix[row_no][column] == 0:
        column = column + 1

    step = -1 # BECAUSE GOING BACKWARD

    for rows in range(row_no-1, -1, step):
        for columns in range(number_of_columns-1, column-1, step):
            Matrix[rows][columns]  = Matrix[rows][columns] - Matrix[rows][column] * Matrix[row_no][columns] / Matrix[row_no][column]

    # USING RECURSION AS MAM MENTIONED IN THE CLASS.
    # for i in range(row_no - 1,-1,-1):
    #     for j in range(number_of_columns - 1,column - 1,-1):
    #         if abs(j) <= 0.00000001:
    #             Matrix[i][j] = 0
    return going_backward(row_no-1, Matrix, number_of_rows, number_of_columns)

# TO GET PIVOTS
def get_pivots(A,row,i,g):
    if A[g][i] == 0:
        return False
    count = 0
    for k in range(row):
        if A[k][i] != 0:
            count = count+1
    if count != 1:
        return False
    else:
        return True

Matrix_info = []
Matrix = []
Size = []
file = open("MATHINPUT.txt")

for line in file:
    Matrix_info = line.strip().split()
    if len(Matrix_info) != 1:
        Matrix.append(Matrix_info)
    else:
        Size.append(int(Matrix_info[0]))
file.close()
number_of_columns = Size[0]
number_of_rows = Size[1]
Matrix = [[int(j) for j in i] for i in Matrix]
print(Matrix)
print("ORIGINAL MATRIX : ")
for i in Matrix:
    print(i)
dict1 = {}
for r in range(number_of_rows):
    col = 0
    while col<number_of_columns and Matrix[r][col] == 0:
        col = col + 1
    dict1[r] = col
    res_dict = {key: val for key, val in sorted(dict1.items(), key = lambda ele: ele[1])}
Matrix = [Matrix[r] for r in res_dict]
Echelon_Form = going_forward(0, Matrix, number_of_rows, number_of_columns)
print("ECHELON FORM : ")

for i in Echelon_Form:
    print(i)

rref_of_Matrix = going_backward(number_of_rows-1, Echelon_Form, number_of_rows, number_of_columns)
print("RREF : ")

for i in rref_of_Matrix:
    print(i)

# TO GET THE GENERAL SOLUTION OF THE MATRIX.
str_ans = ""
ans = []
for i in range(number_of_columns):
    ans.append(0)
index = 0
for i in range(number_of_columns-1):
    if get_pivots(rref_of_Matrix,number_of_rows,i,index) == False:# BECAUSE WE NEED FREE VARIABLES.
        arr = []

        for x in range(number_of_columns):
            arr.append(0)

        arr[i] = 1
        for r in range(number_of_rows):
            if rref_of_Matrix[r][i] != 0:
                arr[r] = -(rref_of_Matrix[r][i])
        free_variable_index = i + 1
        if i != number_of_columns:
            str_ans = str_ans + "X" + str(free_variable_index) + "*" + str(arr) + " + "
        else:
            str_ans = str_ans + "X" + str(number_of_columns+1) + "*" + str(arr) + " + "
        ans[i] = 0
    else:
        ans[i] = rref_of_Matrix[index][number_of_columns-1]
        index = index + 1
print("SOLUTION IN PARAMETRIC VECTOR FORM : ")
str_ans = str_ans + str(ans)
print(str_ans)