#Multiplication and Addition of Matrices
matrices=rows=columns=[]
for m in range(1,3):
    rows.append(int(input("Rows in Matrix "+str(m)+" : ")))
    columns.append(int(input("Columns in Matrix "+str(m)+" : ")))
    print("Enter Elements:")
    matrices.append([[int(input()) for i in range(columns)] for j in range(rows)])
    if(m==2):
        matrices.append([[(matrices[0][i][j]+matrices[1][i][j]) for i in range(columns)] for j in range(rows)])
        matrices.append([[(matrices[0][i][j]+matrices[1][i][j]) for i in range(columns)] for j in range(rows)])

print(matrices[2])
print(matrices[3])