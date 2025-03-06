import numpy as np
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# 1-d Array

nparrray=np.array([1,2,3,4,5,6,7,8,9,10])
for i in nparrray:
    print(i)

for i in range(nparrray.shape[0]):
    print(nparrray[i])

# 2-d Array

nparrray2=np.array([[1,2,3,4,5,6],[2,4,6,7,8,9]])
for i in nparrray2:
    #Rows Printed
    print(i)

for x in nparrray2:
    for y in x:
        #Each Elements in a single row
        print(y)

for i in range(nparrray2.shape[0]):
    for j in range(nparrray2.shape[1]):
        if nparrray2[i][j]==4 or nparrray2[i][j]==8:
            continue
        else:
            print(nparrray2[i][j])

# 3-d Array

nparray3=np.array([[[1,2,3,4],[2,4,6,8]],[[1,3,5,7],[4,8,2,3]]])
# Printing whole array
for x in nparray3:
    print(x)

#printing Each row
for x in nparray3:
    for y in x:
        print(y)

# Printing individual item
for x in nparray3:
    for y in x:
        for z in y:
            print(z)

for i in range(nparray3.shape[0]):
    for j in range(nparray3.shape[1]):
        for k in range(nparray3.shape[2]):
            print(nparray3[i][j][k])

# Printing individual item using np.nditer()
for x in np.nditer(nparray3):
    print(x)
print("Shpae of nparray3: "+str(nparray3.shape))
