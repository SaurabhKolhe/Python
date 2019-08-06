'''
String:
       Collection of character,letter i.e alphabates,numeber i.e alphanumeric value is String.
       String is Immutable.(Means it cannot change.Once we assign value to string then its specific character cannot change.)
       Indexing of string:
                           In python positive and negative both indexing is supported.
                           Index      0  1  2  3  4
                                     |H |E |L |L |O |
                           Index     -5 -4 -3 -2 -1
                           So by indexing we can access specific character inthe string
                           
       Length of String: We can check length of string by:
                         print(len(variable_name))
                         eg.  a="Hello"
                              print(len(a))
                              Output: 5
                              print(a[0])
                              Output:'H'
                              print(a[-5])
                              Output:'H'
                              
       Slicing of String: We can slice string by its index as:
                           variable_name[starting_index:ending_index]     Ending index is exclude from slicing
                           eg.  a="Hello"
                                print(a[0:3])
                                output: Hel
'''

a="Hello"
print("Type of a is ",type(a))
print("Length of a is",len(a))
print("Slicing of string a:")

print("By positive indexing:")
print("a[0:] ",a[0:])
print("a[2:]",a[2:])
print("a[:5] ",a[0:5])
print("a[:3] ",a[:3])
print("a[0:5] ",a[0:5])
print("a[2:5] ",a[2:5])
print("a[0:3] ",a[0:3])
print("a[2:4] ",a[2:4])

print("By Negative indexing")
print("a[-5:] ",a[-5:])
print("a[-3:] ",a[-3:])
print("a[:0] ",a[:0])
print("a[:-2] ",a[:-2])
print("a[-5:0] ",a[-5:0])
print("a[-3:0] ",a[-3:0])
print("a[-5:-2] ",a[-5:-2])
print("a[-3:-2] ",a[-3:-2])
