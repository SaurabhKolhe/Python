'''
List : It contain collection data which having different datatype(can contain same datatype)
       i.e we can add number,string,float,boolean,complex in list.
       As array only contain data of same datatype,it is more useful. (Array not exist in python)
       List is mutable i.e we can change any specific value in list.
       
       Syntax:
              list_name=[...data seperated with comma...]
              eg: a=[10,"String",10.45,True,False,1+4j]
              
       Indexing: List having same indexing as string i.e positive and negative both.
                   index           0     1       2     3    4    5      
                                a=[10,"String",10.45,True,False,1+4j]
                   index          -6    -5      -4    -3   -2    -1  
'''
a=[10,"Hello",10.34,True]
print("List a: ",a)
print("Slicing of list")
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

b=[20,10,30,50,70,40]
#There is sorting function in list 
b.sort()
#There is reverse function in list
b.reverse()
#By sort() we can arrange list in ascending order and to arrange in discending order we can use sort() and then reverse() function.

#we can delete value from list by pop() function
b.pop()
b.pop(2)  #we can give location of value tom delete

#To add any value to list we can use append function
b.append(90)
#To add value at specific location we can use insert() function with 2 parameter i.e location and value
b.insert(2,100)   #(location,value)
#We can add any other list in list:
c=[30,40,20]
b.append(c)    #output: [20,10,100,50,70,90,[30,40,20]]

max(b)  #To find maximum value in list
min(b)  #To find minimum value in list
#To delete list del() function is used
del b

 



