
# FUNCTIONS USED
def interchange(nested_arr,ind_1,ind_2):
    temp = nested_arr[ind_1]
    nested_arr[ind_1] = nested_arr[ind_2]
    nested_arr[ind_2] = temp
    return nested_arr
def scale(l,value):
    emp = []
    for i in l:
        i = i/value
        emp.append(i)
    return emp
def colmax(l):
    l = zip(*l)
    return l
# MULTIPLYING SCALAR C TO THE JTH ROW AND ADDING IT TO THE ITH ROW
def row_operation(Matrix,i,scaler,j):
    a = len(Matrix[0])
    for k in range(a):
        Matrix[i][k] = Matrix[i][k] + scaler*Matrix[j][k]
    return(Matrix)
def rot(arr,n):
    pass
    for i in range (int (n / 2)):
        for j in range (i, int (n - i - 1)):
            # It will swap elements of each cycle in clock-wise direction
            temp = arr[i][j]
            arr[i][j] = arr[n - 1 - j][i]
            arr[n - 1 - j][i] = arr[n - 1 - i][n - 1 - j]
            arr[n - 1 - i][n - 1 - j] = arr[j][n - 1 - i]
            arr[j][n - 1 - i] = temp
    return arr
# STEP 1
# CREATING THE INITIAL MATRIX

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

Matrix = [[int(j) for j in i] for i in Matrix]
print(Matrix)
print("THE INITIAL MATRIX A IS A ",Size[0], "BY", Size[1],"MATRIX")
print()
print("THE CONTENTS OF THE MATRIX ARE AS FOLLOWS : ")
print()

for row in Matrix:
    for item in row:
        print(item,end = "  ")
    print()
    print()
length = len(Matrix)
# STEP 2
# APPLYING ROW REDUCTION ALGORITHM ON THE MATRIX A TO GET THE RREF MATRIX
# TO GET THE LEFTMOST NON ZERO COLUMN OR WE CAN JUST OPERATE AT INDEXES AND SAVE THOSE OPERATIONS TO OPERATE AT OTHER INDEXES
for i in range(0,length-1):
    # APPLYING THE PARTIAL PIVOT METHOD MENTIONED IN THE NUMERICAL NOTE OF THE ROW REDUCTION ALGORITHM IN DAVID C.LAY
    if abs(Matrix[i][i] < 0.0000000000000001):
        for j in range(i+1,length):
            if abs(Matrix[j][i]>abs(Matrix[i][i])):
                Matrix = interchange(Matrix,j,i)
                break
    for j in range(i+1,length):
        if Matrix[j][i] == 0:
            # Move to the next row
            continue
        opr = Matrix[i][i]/Matrix[j][i]
        for k in range(i,length):
            Matrix[j][k] = Matrix[i][k] - Matrix[j][k]*opr

# for i in range(length-1,-1,-1):
for i in Matrix:
    print(i)
for i in Matrix:
    for j in i:
        if j != 0:
            Matrix[Matrix.index(i)] = scale(Matrix[Matrix.index(i)],j)
            break
for i in Matrix:
    print(i)
# Matrix = row_operation(Matrix,0,-1.6666666666666667,1)
print(Matrix)
arr = rot(Matrix,length)
print(arr)