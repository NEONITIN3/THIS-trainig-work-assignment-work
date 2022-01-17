class Emp():
  def display(self):
      print("This is from Base class")

class Manager(Emp):
    def display1(self):
        print("This is from Sub class")

cla = Manager()
cla.display()
cla.display1()