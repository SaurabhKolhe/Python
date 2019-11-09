'''
Logical operator:
                 There are 3 types of logical operators in python
                 1.and:
                       It will check both sides is true or not if yes it will return True
                       p  and   q        result

                       T        T           T
                       F        T           F
                       T        F           F
                       F        F           F

                 2.or:
                      It will check any one sides is false or not if yes it will return True
                       p   or   q        result

                       T        T          F
                       F        T          F
                       T        F          F
                       F        F          T

                 3.not:
                       It is gives negation of given number.
                    not p      result

                        T         F
                        F         T

'''
a=20
b=20
c=20
d=10
if a==b and b==c:
    print("and operator works")
else:
    print("Condition failed")

if a==b or b==d:
    print("or operator works")
else:
    print("Condition failed")