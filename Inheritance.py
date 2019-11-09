'''
first preference will be give to its member
same name Function  are not valid
'''

class A:
    def show(self):
     print("hi")
class B(A):
    def show(self):
     print("hi from B")
    def show1(self):
        print("hello")
b=B()
b.show()
b.show1()




