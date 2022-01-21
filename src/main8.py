import math
import numpy as np
#import matplotlib as mpl
#import matplotlib.pyplot as plt

dir()
help(math.acos)

#l = [1, "alfa", 0.9, (1, 2, 3)]
#print(type(i) for i in l)

a=np.array([[1,2],[2,2]])
print(a.shape)
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b.shape)
print(b.itemsize)
print(b.dtype)
print(b.strides)

a = np.array([1,2,3,4])
list1 = [1,2,3,4]
tupla = (5,6,7,8)
a = np.array(list)
b = np.array(tupla)
c = np.array([list1,tupla])
print(c)
print(a.dtype)

vec=np.arange(0,5,1, dtype=None)
print(vec)
print(np.fromstring('1 2', dtype=int, sep=' '))

b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Sum " ,b,"+",c, "= ", b+c)
b+=1
print("Autoincrement b +=1 b=", b)
print("Multiply c*3 " ,c, "* 3= ",c*3)
print("Sin (c)", np.sin(c))

a=np.array(range(1,9))
#c_style = a.reshape((2,2,2),order=‘C’)

v1=np.array([1,2,3])
v2=np.array([10,20,30])
print(v1*v2)
print(np.dot(v1,v2))
a = np.ones(4)
print(a)
mat=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(mat[0][0])

a=np.arange(25)
a=a.reshape((5,5))
print(a)

a=np.arange(5)
a: [0,1,2,3,4]
b=a
b[0]=100
print ("a:", a , "b:" , b)