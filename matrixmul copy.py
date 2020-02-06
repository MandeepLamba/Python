#Multiplication and Addition of Matrices
matrices = []
rowcol = int(input("Rows & Columns in Matrix: "))
for m in range(2):
    # columns = int(input("Columns in Matrix "+str(m)+" : "))
    print("Enter Elements of Matrix "+str(m+1)+": ")
    matrices.append([[int(input()) for i in range(rowcol)] for j in range(rowcol)])
    # if(m==1):
matrices.append()
for i in range(rowcol):
    for j in range(rowcol):
        for k in range(rowcol):
            matrices[2][i][j]+=matrices[0][i][k]*matrices[1][k][j]

print(matrices[2])