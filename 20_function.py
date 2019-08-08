'''
Function:
         When some lines of code in required in program repeately then we can write it in function.
         Function is reduce complexity of program.
         There are 2 types of function:
         1.Pre_define Function:
                               It is function which are already define in language/library.
                               Functions like print(),input(),randint(),math(),etc are predefine functions.
         2.User_define Function:
                                It is function which created by user for repeately use and reduce complexity.
                                user define function always comes with def keyword followed by identifier(any name of function)
                                We cannot creat null function in python.
                                To use function we have to just call that function.
                                Syntax:
                                       def function_name():             #Function Defination
                                          .........code.......
                                          .........code.......
                                          .........code.......
                                       function_name()                  #Function call
'''
#Simple program to print hello through function 
print("Start!!!")
def hello():
    print("Hello")
hello()
print("End!!!")

#There are 4 types of User_define functions

#1.function witout parameter and without return value
print("Start!!!")
def small():
    print("Hey i am small")
small()
print("End!!!")

#2.function witout parameter and with return value
print("Start!!!")
def small_return():
    a=5
    return a
b=small_return()     #we are storing return value from small_return function in b
print(b)             #It will print 5 
print("End!!!")

#3.function with parameter and without return value
#Program to find square of given number
print("Start!!!")
c=int(input("Enter number to find square"))
def sqr(x):
    x=x*x
    print("x")
hello(c)
print("End!!!")

#4.function with parameter and with return value
#program to find cube of given number
print("Start!!!")
e=int(input("Enter the number to find cube"))
def cube(y):
    y=y*y
    return y
d=cube(e)
d=d*d
print("d")
print("End!!!")
print("\n")

#Arithmetic operation using function
print("Arithmetic operation using function")
p=int(input("Enter 1st Number"))
q=int(input("Enter 2nd Number"))
def add(p,q):
         print("Addition : "a+b)
def sub(p,q):
         print("Substraction : "a-b)
def mul(p,q):
         print("Multiplication : "a*b)
def div(p,q):
         print("Division : "a//b)
add(p,q)
sub(p,q)
mul(p,q)
div(p,q)

        
