'''
Constant:
         Value which is not change after declaration.
         But constant variable is not supported in python.
         1.Just for understanding of constant variable we can write it in capital i.e.
         APP=123
         It can change but it only shows that this variable is constant i.e. final (not for change)
         2.Another way to constant variable is to declare it in another file and then import that file.

'''
#First way of making constant variable.
ROLL = 23
NAMES = "SAURABH"

#Second way of making constant variable.
import const
a=const.APP
b=const.NAME
print(a)
print(b)

import const as c    #we using c as reference of const
c=c.APP
d=c.NAME
print(c)
print(d)

