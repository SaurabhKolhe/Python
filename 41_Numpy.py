'''
Never give file name similar to module name.
eg. numpy,array,pandas,matlab,List,etc.

numpy:
      1.It is extended version of array.
      2.It is use for do complex numeric calculation like matrix operation
      3.numpy library is written in C language
      4.It is use in data science
      To install numpy:
        pip3 install numpy (windows powershell (windows icon>R_click>select windows powershell))

      To install in pycharm:
        setting>project>project interpreter> + > numpy > install
'''
import numpy as np

val = np.array([1, 2, 6, 8])
val1 = np.array([1, 2, 6, 8])
a = val + val1
b = val - val1
c = val * val1
d = val / val1
e = val // val1
print(a)
print(b)
print(c)
print(d)
print(e)
val2=np.array([[1,2],[4,9]])
val3=np.array([[1,2],[4,9]])
d=val2+val3
print(d)
#To find dimension of array eg. 1dimensional,2dimensional
print(val.shape)
print(val1.shape)

val4=np.zeros([5,5])
print(val4)
val5=np.ones([5,5])
print(val5)
