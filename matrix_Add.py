#Add 2 metrices

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[2,2,2],[3,3,3],[1,1,1]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        r[i][j]=a[i][j]+b[i][j]

print(r)
