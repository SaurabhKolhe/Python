'''
doc string:
           It is use to print comment write in first line of function.
           It is mainly use for get information about function where we give in comment
           Syntax:
                  def fun_name():
                      #........comment about function.........
                      ..........code....................
                  print(fun_name.__doc__)    #we use 2 times '_' before after doc
'''
def fun():
    '''This function is used to known about doc string'''
    print("Hii")
print(fun.__doc__)
