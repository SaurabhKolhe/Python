'''
Loops:
      Some lines of code we want use repeately upto certain condition then we use loop.
      Ther are 3 types of loops:
      1.while
      2.for
      3.do while.
      
While loop:
           Syntax:
                  ................code..............
                  initialization
                  while (condition):                          #() is optional but in standard way is to not use ()
                      ................code..........
                      ................code..........
                      ................code..........
                      increament/decrement
                  ..........code.................... 

Drawback:
        We have initialize one variable.
        continue in not working in while.

'''
#To print 1 to 10 number
print("Start!!!")
a=1
while a<11:
    print(a)
    a=a+1                   #a++/a-- is not supported in python.
print("End!!!")

#To break a while loop at specific condition
print("Start!!!")
a=1
while a<=10:
    if a==8:
        break
    else:
        print(a)
    a=a+1
print("End!!!")

#To pass specific condition in while loop
print("Start!!!")
a=1
while a<=10:
    if a==8:
        pass
    else:
        print(a)
    a=a+1
print("End!!!")
