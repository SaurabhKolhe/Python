#To give grade according to percentage
a=int(input("Enter your percentage"))
if a>70:
    print("You got First class with Distinction")
elif a>50 and a<70:
    print("You got First class")
elif(a<35 and a<50):
    print("You got Second class")
else:
    print("You are Failed in Exam")
    
