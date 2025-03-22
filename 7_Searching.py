import numpy as np
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

nparray=np.array([0,1,2,3,4,5,6,7,8,9,10,7,8,7])
x=np.where(nparray==5)
print(nparray)
print(x) 

print(x[0]) # Return only index number

y=np.where(nparray==7)
print(y)
print(nparray[y]) # Return the actual item

# Return Even Position number
z=np.where(nparray%2==0)
print(nparray)
print(z[0])
# Return Odd Position Number
z=np.where(nparray%2==1)
print(nparray)
print(z[0])
