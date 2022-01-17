class Emp:
    def display(self,name=None,salary=None): # parameter
      if name ==None and salary ==None:
          print("This is default method")
      elif name!=None and salary ==None :
          print("Name is : " , name)
      else:
          print("Name is : " , name)
      print("Salary is : " , salary)


cla = Emp()
cla.display()
print()
cla.display(input("Enter Name : ")) # argu
print()
cla.display(input("Enter Name : "),int(input("Enter Salary : ")))