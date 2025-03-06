import sys
import numpy as np
# Redirect standard input and output to files
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


list1=[1,2,"name",3,4]
list2=["ne",list1,34,True]

print(np.array(list1))

print(np.arange(10))

print(np.arange(0,10,3)) # 0 to 10 with a specific step size 

print(np.zeros(10))

print(np.zeros((4,10))) # np.zeros((x,y)) x dimensions and each dimensions carry y number elements

#not zeros

print(np.full((11,10),8)) # np.full((x,y),z) x dimension and y elements in each dimensions and z is the elements

#python list to numpy

my_list=[8,4,5,6,7]
print(np.array(my_list))
