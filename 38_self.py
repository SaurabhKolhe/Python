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
