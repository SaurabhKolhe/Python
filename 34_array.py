'''
Array:
    In c/c++/Java:
      It is collection of same kind of data(datatypes).
      int a[10]=[];   (c/c++)
      int a=new a[];  (Java)
      We cannot change size of array after it allocate.
      We can add same kind of data in aaray.
      In Java we can use ArrayList for store different kind of data(Heterogenious data) and change its size.
    In Python:
            1.Array not directly support in python we have to import aaray in python
            eg. from array import *
            2.It support homogenous data i.e. same kind of Data but here we can change its size.
            3.It is mutable.
            4.It support both positive and negative indexing.

            from array import *
            variable_name=array('datatype',["data"])
            val=array('i',[1,2,3,4])
            print(val[0])

            Disadvantages:
                1.Multidiamensional array is not support in python.
                2.It is complex structure to remember.
                3.We have to remember many keyword about Datatype.

    WE ARE USING NUMPY RATHER THAN ARRAY WHICH IS EXTENDED VERSION OF ARRAY.
'''
from array import *

val=array('i',[1,2,3])

print(val[0])
print(val.buffer_info)

#To add value in array
val.append(5)
print(val)

#To add value in particular location
val.insert(0,8)  #(location,element)
print(val)

#To reverse array
val.reverse()
print(val)

#To delete last element
val.pop()
print(val)

#To delete value from particular location
val.pop(2)
print(val)

#To find count
print(val.count(1))
