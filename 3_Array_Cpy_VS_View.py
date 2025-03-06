import numpy as np
import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')


nparray=np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8])
# nparray2=nparray.view()
# # create view
# # print(f'original nparray {nparray}')
# # print(f'original nparray {nparray2}')

# # nparray[0]=90

# # print(f'changed nparray {nparray}')
# # print(f'original nparray {nparray2}')

#create Copy

nparray2=nparray.copy()
print(f'original nparray {nparray}')
print(f'original nparray {nparray2}')

nparray[0]=88
print(f'changed nparray {nparray}')
print(f'original nparray {nparray2}')

#again creating view
nparray3=nparray2.view() ## Both arrray are connected in both ways
print(f'Original nparray2 {nparray2}')
print(f'original nparray3 {nparray3}')

nparray3[0]=69
print(f'Original nparray2 {nparray2}')
print(f'Changed nparray3 {nparray3}')