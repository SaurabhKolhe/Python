#List
c=[]
a=int(input("Enter size of list"))
for i in range(a):
    b=int(input("Enter number to add in list"))
    c.append(b)
print(c)

#
val=int(input("Enter the number you want to search"))
if val in c:
    print("Available")
    print(c.index(val))   #to know position of val
else:
    print("Number is not available")

#Operation on List
print("Sorting of List")
c.sort()
print(c)
print("Reverse of List")
c.reverse()
print(c)
max=c[0]
for i in range(1,a):
    if c[i]>max:
        max=c[i]
print("Maximum number in List ",max)
temp=0
for i in range(a):
    temp=temp+c[i]
avg=temp/a
print("Average of number in List ",avg)



