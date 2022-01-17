class Emp:
    pub = None
    _pro = None
    __pri = None

def __init__(self, pub, pro, pri):
    self.pub = pub
    self._pro = pro
    self.__pri = pri

def displayPublic(self):
    print("Public Data Member: ", self.pub)

def _displayProtected(self):
    print("Protected Data Member: ", self._pro)

def __displayPrivate(self):
    print("Private Data Member: ", self.__pri)

def accessBaseMembers(self):
    self.displayPublic()
    self._displayProtected()
    self.__displayPrivate()

class Manager(Emp):
    def __init__(self, pub, pro, pri):
        Emp.__init__(self, pub, pro, pri)

def accessSubMembers(self):
    self.displayPublic()
    self._displayProtected()
#self.__displayPrivate() # Error
obj = Manager(input("Enter Name 1 :"),input("Enter Name 2 :"),input("Enter Name 3 :"))
obj.accessBaseMembers()
obj.accessSubMembers()
