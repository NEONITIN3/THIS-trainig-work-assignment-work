class Convert:
    def __init__(self): # default constructor
        self.str1 = ""

    def get(self):
        self.str1 = input("Enter Name in Lower case : ")
    def printupper(self):
        print("its your upper case o/p=",self.str1.upper())
str1=Convert()
str1.get()
str1.printupper()

