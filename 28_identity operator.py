'''
Identity operator:
                1.is
                2.not is
'''
a=10
b=10
if a is b:
    print("Same")
else:
    print("Not same")

c=10
d=20
if c is not d:
    print("Not same")
else:
    print("Same")
