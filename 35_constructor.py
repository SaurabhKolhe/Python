'''
Constructor:
            It is method/function in class which execute by just creating object of class.
            Constructor not need to call manually.
            
            Syntax:
                    class A:
                        def __init__(self):
                            ....logic...
                        def show():
                            ....logic....
                        a=A()
                        a.show()
'''

class A:
    def __init__(self):
      print("hi")
    def show():
        print("hello")
class B:
    def __init__(self):
        print("hey i am b")
    def put(self):
        print("hello b")
a=A()
b=B()
