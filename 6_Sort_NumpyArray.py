import numpy as np
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

nparray=np.array([[3,1,5,7,8],[8,4,1,0,8]])
print(np.sort(nparray))

#Alphabetical
list=["john","arya","Sansa","Bran","Theon"]
nparray2=np.array(list)
print(nparray2)
print(np.sort(nparray2)) # Block letter to small letter

#boolean
nparray3=np.array([True,False,True,False])
print(nparray3)
print(np.sort(nparray3))
#2d array
nparray4=np.array([[0,1,8,2,4,6,3,9,0],[4,1,3,2,8,3,6,1,9]])
print(nparray4)
print(np.sort(nparray4)) #Sort inside each individual row