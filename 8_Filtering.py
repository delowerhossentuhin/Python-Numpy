import numpy as np
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

nparray=np.array([1,2,3,4,5,6,7,8,9,10])
print(nparray)
x=[False,True,False,True,False,False,True,False,True,False]
print(nparray[x])
print(nparray[~np.array(x)])


# Filtering using logic

filter=[]
for i in nparray:
    if i%2==0:
        filter.append(True)
    else:
        filter.append(False)

print(nparray)
print(filter)
print(nparray[filter])

# Using Shortcut!!!!!!
filtered=nparray>3
print(nparray)
print(filtered)
print(nparray[filtered])