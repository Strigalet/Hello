x=[]
y=[]
coordinates=[]
i=0
while i < 8 :
    coordinates.append(input().split())
    i=i+1
a=0    
for a in range(0,8):
    x.append(int(coordinates[a][0]))
    y.append(int(coordinates[a][1]))

res="NO"
    
for j in range(0,8):
    for f in range(j+1,8):
        if (abs(x[j]-x[f])==abs(y[j]-y[f])) or (x[j]==x[f]) or (y[j]==y[f]):
            res="YES"
print(res)
