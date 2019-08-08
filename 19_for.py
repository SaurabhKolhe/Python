'''
For Loop:
    1.Syntax:
            .........code.........
            for i in range(number):                  #i start with 0 and number-1 is end
                ....code....
                ....code....
            ...........code........
    In range one parameter is mandatory.
    Ther is no decrement in for loop.
'''
#To print 0 to 9
print("Start!!!")
for i in range(10):               #i is initialize with 0 and 10 is exclude from loop
        print(i)
print("End!!!")

#When want to start with 1
print("Start!!!")
for i in range(1,10):           #here i is initialize from 1 and 10 is exclude i.e. upto 9 it will print
        print(i)
print("End!!!")

#To take interval
print("Start!!!")
for i in range(1,10,2):            #third parameter to interval
    print(i)
print("End!!!")

print("Start!!!")
for i in range(10,1,-1):           #third parameter to interval
    print(i)
print("End!!!")

#To break for loop at specific condition
print("Start!!!")
for i in range(1,10):
    if i==5:
        break
    else:
        print(i)
print("End!!!")

#To pass for loop at specific condition
print("Start!!!")
for i in range(1,10):
    if i==5:
        continue
    else:
        print(i)
print("End!!!")

#To print number which divisible by 3
print("Start!!!")
for i in range(1,22):
    if i%3==0:
        print(i)
print("End!!!")

#To print List using for loop
print("Start!!!")
a=[10,20,30,40]
print(a)
for i in a:
    print(i)
print("End!!!")

#To print Tuple using for loop
print("Start!!!")
b=(10,20,30,40)
print(b)
for i in b:
    print(i)
print("End!!!")
