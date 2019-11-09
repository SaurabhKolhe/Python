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

class A:
    def __init__(self):
      print("hi")
    def show():
        print("hello")
class B(A):
    def __init__(self):
        print("hey i am b")
    def put(self):
        print("hello b")
a=B()
a.put()

# multi level
class A:
    def __init__(self):
        print("hi")
    def show():
        print("hello")
class B:
    def __init__(self):
        super.__init__()
        print("hey i am b")
    def put(self):
        print("hello b")
class C(A,B):
    def put(self):
        print("hello b")
c = C()
'''

# in multiple inhertiance the priority is given to first  and
#   at a one time one constructor is called
# super.__init__(): we can call parent constructor

class A:
    name=None
    id=None
    def __init__(self):
        self.name = "ABC"
        self.id = 123
    def showData(self):
        print("Name is",self.name)
        print("Id is",self.id)
    def updateInfo(self,name,id):
        self.name=name
        self.id=id
a=A()
a.showData()
a.updateInfo("PQR",456)
a.showData()
