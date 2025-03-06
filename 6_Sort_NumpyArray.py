import numpy as np
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

nparray=np.array([[3,1,5,7,8],[8,4,1,0,8]])
print(np.sort(nparray))