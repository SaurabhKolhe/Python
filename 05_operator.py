'''
Arithmetic Operator:
    1.Addition          +
    2.Substraction      -
    3.Multiplication    *
    4.Division          /  (gives answer in float eg. 2/2=1.0)
                        // (gives answer in integer eg.2//2=1)
    5.mod               %
    6.power to          ** (gives power of number eg.2*3=8)

Conditional Expressions:
                          Meaning Math                  Symbol	  Python Symbols
                          Less than	                     <	      <
                          Greater than	                 >	      >
                          Less than or equal	           ≤	      <=
                          Greater than or equal	         ≥	      >=
                          Assignment(Equals)	           =	      ==
                          Not equal	                     ≠	      !=
                          
logical operator:
    1.and  
          p   q    result
          T   T      T
          T   F      T
          F   T      T
          F   F      F

    1.or  
          p   q    result
          T   T      T
          T   F      F
          F   T      F
          F   F      F

    1.not  (!)  
          p     result
          T       T
          T       T     
      
Identity Operator:
    1.is
    2.is not

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

Membership Operator:
    1.in
    2.not in

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
'''
