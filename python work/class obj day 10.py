class Employee:
    no_emp = 0
    raise_amt = 0.05

    def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay
        Employee.no_emp += 1

    def cal_pay(self):
        self.pay = self.pay + (self.pay + self.raise_amt)

    @classmethod
    def set_raise_amt(self, amt):
        self.raise_amt = amt

    @classmethod
    def from_str_val(self, emp_str):
        first, last, email, pay = emp_str.split(",")
        return self(first, last, email, pay)

    def display(self):
        print(self.first)
        print(self.last)
        print(self.email)
        print(self.pay)


emp1 = Employee("sam", "Luke", "sam@gmail.com", 30000)
emp2 = Employee("John", "Vick", "john@gmail.com", 40000)
emp1.display()
emp2.display()
print(Employee.raise_amt)
Employee.set_raise_amt(0.07)
emp_str1 = input("Enter the fname,lname,email,pay: ")
emp_str2 = input("Enter the fname,lname,email,pay: ")
emp3 = Employee(emp_str1)
emp4 = Employee(emp_str2)
emp3.display()
emp4.display()
