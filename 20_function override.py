#Function overriding is not Supported in python


def add():
    print("Hiii")
def add(a):
    print(a)
add(8)
# add()    This will give error

'''
add() function is replace by add(a) as our program run from top. 
so it will give error when we call add()
'''
