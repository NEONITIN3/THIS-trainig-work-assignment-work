class Employee:
    def __init__(self, sal):
        self.sal = sal

# def setage(self, inc)
# self.inc = inc

def __add__(self, obj):
    return Employee(self.sal + obj.sal)

def __gt__(self, obj):
    return self.sal > obj.sal

def __lt__(self, obj):
    return self.sal < obj.sal

def __str__(self):
    return "Highest Salary " + str(self.sal)


emp_1 = Employee(5000)
print(emp_1.sal)

emp_2 = Employee(10000)
print(emp_2.sal)

emp_3=emp_1 + emp_2
print(emp_3.sal)

print(emp_3 > emp_2)

print(emp_1 < emp_2)

print(emp_3)
