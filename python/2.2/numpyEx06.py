import numpy as np
# A = np.array([[1, 2, 3], [4, 5, 6]])

# print(A)
# print(A.T)

# a=np.arange(12)
# print(a)
# print(a.reshape(3,-1))
# print(a.reshape(2,2,-1))
# print(a.reshape(2,-1,2))

a = np.zeros([12,5])
print(a)
a[:, 3:] = 1
print(a)

b = [[10,20,30,40,50],
     [60,70,80,90,100],
     [110,120,130,140,150]]
a[3:6,:] = b
a[9:12,:] = b 
print(a)
