'''
Abstraction:
            To hide some data.
            We only declare function in abstract class and we can define it when needed.
Interface:
         It Only contain all function with declaration.

Difference between Abstract Class and Interface:
                            Abstract Class                    Interface
           constructor        support                       not supported
           object             support                       not supported
           function       define and undefine function      only define function
'''
class person:
    def showProf(self):
        pass
class Doctor(person):
    def showProf(self):
        print("Doctor")
class Engineer(person):
    def showProf(self):
        print("Engineering")
a=Engineer()
a.showProf()
b=Doctor()
b.showProf()