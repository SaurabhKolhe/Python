#To give grade according to percentage
print("Start!!!")
a=int(input("Enter your percentage"))
if a>70:
    print("You got First class with Distinction")
elif a>50 and a<70:
    print("You got First class")
elif(a<35 and a<50):
    print("You got Second class")
else:
    print("You are Failed in Exam")
print("End!!!")
print("\n")

#Calculator using if else
print("Calculator using if else and elif")
p=int(input("Enter 1st Number\t"))
q=int(input("Enter 2nd Number\t"))
r=input("Operation\t")
if r =='+':
    print("Addition:",p+q)
elif r =='-':
    print("Substraction:",p-q)
elif r == '*':
        print("Multiplication:",p*q)
elif r == '//':
        print("Division in Integer:",p//q)
elif r == '/':
        print("Division in Float:",p/q)
elif r == '%':
        print("Remainder of division:",p%q)

