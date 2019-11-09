'''
Multithreading
1.main process in which small task can be proceed
2.a process start execution parallely is called multithreading
3.at one time a thread is executing sequential(i.e one after another )
4.in one task if there are more task we can define it as multithreading
5.it gives equal time to all task

In python bydefault threading is not supported

from threading import *
class A (thread):
    def run(self):
    ..........logic....
class B (thread):
     def run(self):
     ..........logic.....
a=A()
a.start()
b=B()
b.start()

multithreading program
from threading import * = package name
class A (Thread):
    def run(self):
        for i in range (500):
            print("A1")
class B (Thread):
     def run(self):
        for i in range(500):
            print("A2")
a=A()
a.start()
b=B()
b.start()

a.start= it touches and again go ahead
a.run=behaves as normal function it execute function till it executes all
only Independent task can execute in multithreading
Dependent task cannot be execute in multithreading
'''
from threading import *
class A (Thread):
    def run(self):
        for i in range (500):
            print("A1")
class B (Thread):
     def run(self):
        for i in range(500):
            print("A2")
a=A()
a.start()
b=B()
b.start()
