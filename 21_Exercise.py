#Creating List with userdefine size
c=[]
a=int(input("Enter size of list\t"))
for i in range(a):
    b=int(input("Enter number to add in list\t"))
    c.append(b)
print(c)

#Find number and location in List
val=int(input("Enter the number you want to search\t"))
if val in c:
    print("Available")
    print(c.index(val))
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
min=c[0]
for i in range(1,a):
    if c[i]<min:
        min=c[i]
print("Minimum number in List ",min)
temp=0
for i in range(a):
    temp=temp+c[i]
avg=temp/a
print("Average of number in List ",avg)



