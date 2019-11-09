'''
Membership operator:(in,not in)
'''
#List
val=20
value=50
a=[10,20,30,40]
if val in a:
    print("Available")
    print(a.index(val))   #to know position of val
if value not in a:
    print("Not Available")

#Tuple
b=(10,20,30,40)
val=40
value=50
if val in b:
    print("Available")
if value not in b:
    print("Not Available")

#Dictionary
a={"name":"aasem","age":22}
b="name"
c="name1"
if val in b:
    print("Available")
if value not in c:
    print("Not Available")

