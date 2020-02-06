#Multiplication and Addition of Matrices

matrices = []
rowcol = int(input("Rows & Columns in Matrix: "))
for m in range(2):
    print("Enter Elements of Matrix "+str(m+1)+": ")
    matrices.append([[int(j) for j in input().split()] for i in range(rowcol)])

matrices.append([[(matrices[0][i][j]+matrices[1][i][j]) for j in range(rowcol)] for i in range(rowcol)])
matrices.append([[sum(matrices[0][i][k]*matrices[1][k][j] for k in range(rowcol)) for j in range(rowcol)] for i in range(rowcol)])

print("Sum: ",matrices[2])
print("\nMul: ",matrices[3])