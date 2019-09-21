#Username and Password Validation
user=input("Enter Username\t")
passw=input("Enter Password\t")
if user=="admin" and passw=="admin":
    print("Welcome!!!")
else:
    print("Incorrect Username or Password")

#Validation of password,mobile number and username
user1=input("Enter Username\t")
if len(user)<4:
    print("Please enter Username greater than 4 character")
passw1=input("Enter Password\t")
cpass1=input("Confirm Password\t")
if passw1!=cpass1:
    print("Password not matched")
mob=input("Enter mobile number")
if len(mob)!=10:
    print("Mobile Should be 10 digit")
mob=int(mob) 

