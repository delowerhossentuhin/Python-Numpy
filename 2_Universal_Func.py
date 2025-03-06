import numpy as np
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

npArray=np.array([-4,-3,-2-1,1,2,3,4,5,6,7,8,90])

# print(np.sqrt(npArray,where=npArray>=0))
# print(np.sqrt(np.absolute(npArray)))
# print(np.square(npArray))
# print(np.absolute(npArray))

# a=int(input())
# print(np.absolute(a))
# print(np.exp(npArray),end="")
# print(np.exp(npArray[0]))
# print(np.max(npArray))
# print(np.min(np.absolute(npArray)))
print(npArray)
print(np.sign(npArray))

#Trig  sin cos tan log
print(np.round(np.cos(np.deg2rad(npArray)),10))

print(np.round(9.1))
print(np.log(np.absolute(npArray))) ##log 0 is infinity

