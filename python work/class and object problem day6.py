class ms:
    total_emp=0
    basic_hike=0.08
    def __init__(self,first,last,email,position,bsalary):
        self.fname=first
        self.lname=last
        self.eid=email
        self.domain=position
        self.pay=bsalary
        #after calling shoud be increases the emp count
        ms.total_emp +=1
    #hike calculate
    def now_pay(self):
        self.totalsalary=self.pay*ms.basic_hike+self.pay

    def display(self):
        print(self.fname)
        print(self.lname)
        print(self.eid)
        print(self.domain)
        print(self.pay)
        # print(self.per)
        print(f"Currently number of emp is= {ms.total_emp}")
        print(f"for {self.fname} now total salary is {self.totalsalary}")

emp1=ms("Ram","chandra","raam@gmail.com","DevOps",1200000)
emp1.now_pay()
emp1.display()
#print(ms.total_emp)
emp2=ms("Sam","chandra","raam@gmail.com","DevOps",1200000)
emp2.now_pay()
emp2.display()
# print(ms.total_emp)
#way of printing and call particular object
#1
emp1.now_pay()
emp2.now_pay()
emp1.display()
emp2.display()

#2
ms.display(emp1)
ms.display(emp1)

if we want particular hike for particular emp
emp1.basic_hike=0.10
print(emp1.__dict__)
print(emp2.__dict__)
print(emp1.__doc__) #none
print(emp1.totalsalary)
print(emp2.totalsalary)