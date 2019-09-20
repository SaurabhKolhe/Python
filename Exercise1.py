#Username and Password Validation
'''user=input("Enter Username\t")
passw=input("Enter Password\t")
    if user=="admin" and passw=="admin":
        print("Welcome!!!")
    else:
        print("Incorrect Username or Password")
'''


user=input("Enter Username\t")
passw=input("Enter Password\t")
cpass=input("Confirm Password\t")
if passw!=cpass:
    print("Password not matched")

