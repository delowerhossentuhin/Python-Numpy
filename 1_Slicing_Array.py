import numpy as np
import sys

sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

npArray=np.arange(4,30,3) #output [ 4  7 10 13 16 19 22 25 28]

""" #slicing 
print(npArray[1:5]) # 1st element to (5-1)th element
print(npArray[0:]) #return till the end

#print backward
print(npArray[-4:-1]) # 19 22 25
#steps
print(npArray[1:8:3]) #slicilung with steps
print(npArray[::2]) # entire array with steps """

#slicing 2d array
npArray2=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]])
#pull out a single element
print(npArray2[1,2])# 8

#slicing
print(npArray2[1:2,2:5])

#slice from both
print(npArray2[0:2,0:5:2])