import numpy as np
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
#create 1-D array and get it's shape
nparray=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(nparray)
print(nparray.shape)
#create 2-D array and get it's shape [Return Rows / Column]
nparray2=np.array([[1,2,3,4,5],[2,4,6,8,10],[1,3,5,7,9]])
print(nparray2)
print(nparray2.shape)
#Reshape 2-D array
nparray3=nparray.reshape(2,6)
print(nparray3)
print(nparray3.shape)
#Reshape 3-D array
nparray4=nparray3.reshape(3,2,2)
print(nparray4)
print(nparray4.shape)

#Flatten to 1-D
nparray5=nparray4.reshape(-1)
print(nparray5)
print(nparray5.shape)

nparray6=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
print(nparray6.shape)
nparray6=nparray6.reshape(4,3,2,1)
print(nparray6)