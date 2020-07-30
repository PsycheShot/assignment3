row = int(input("Enter the no of rows: "))
col = int(input("Enter the no of columns: "))

matrix=[]

for i in range(row):
    r = []
    for j in range(col):
        r.append(int(input()))
    matrix.append(r)
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()

print(max(max(matrix)))
print(min(min(matrix)))
cmax=[]
rmax=[]
rmin=[]
cmin=[]
for i in range(row):
    rmax.append(max(matrix[i]))
    rmin.append(min(matrix[i]))
for i in range(col):
    maxi = matrix[0][col-1]
    mini = matrix[0][col-1]
    for j in range(0,row):
        maxi = max(maxi,matrix[j][i])
        mini = min(mini,matrix[j][i])
    cmax.append(maxi)
    cmin.append(mini)        
        


print(rmax)
print(rmin)
print(cmax)
print(cmin)