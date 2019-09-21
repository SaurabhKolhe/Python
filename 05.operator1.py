'''
1.Formatting of string:
                     1.format
                     2.f
'''
a=10
b=20

#When we want to print 1 variable
print("Value of A: ",a)

#When we want to print 2 value a and b then we can write:
print("Value of A: and B: ",a,b)
#But it is not giving in proper way

#So We can use 'format' for print it in proper way
print("Value of A:{} and B:{} ".format(a,b))

#When we want to print more than 3 variable
print("Value of A:{} B:{} A:{} A:{} B:{} B:{}".format(a,b,a,a,b,b))
#It will print in proper wqay but it will very confusing as we want to keep in mind we which function come in which time

#Other way to write that type of program is using f"":
print(f"Value of A:{a} B:{b} A:{a} A:{a} B:{b}")
#It is more easier than 'format'

'''
2.doc string:
           It is use to print comment write in first line of function.
           It is mainly use for get information about function where we give in comment
           Syntax:
                  def fun_name():
                      #........comment about function.........
                      ..........code....................
                  print(fun_name.__doc__)    #we use 2 times '_' before after doc
'''
def fun():
    '''This function is used to known about doc string'''
    print("Hii")
print(fun.__doc__)
