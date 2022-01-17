
emp1,emp2,emp3=input("enter the 3 emp name = ").split(",")
exp1,exp2,exp3=input("enter the year of exp= ").split(",")
salary1,salary2,salary3=input("enter the salary = ").split(",")
if(int(exp1)>=5):
           salary1=int(salary1)+(int(salary1)*.3)
           print("salary for" ,emp1,"for",exp1,"of expr","is = " ,salary1)
elif(int(exp1)>=2 and int(exp1)<5):
    salary1=int(salary1)+(int(salary1)*.2)
    print("salary for" ,emp1,"for",exp1,"of expr","is = " ,salary1)
    
if(int(exp2)>=5):
           salary2=int(salary2)+(int(salary2)*.3)
           print("salary for",emp2,"for",exp2,"of expr","is = " ,salary2)
elif(int(exp2)>=2 and int(exp2)<5):
    salary2=int(salary2)+(int(salary2)*.2)
    print("salary for",emp2,"for",exp2,"of expr","is = ",salary2)

if(int(exp3)>=5):
           salary3=int(salary3)+(int(salary3)*.3)
           print("salary for",emp3,"for",exp3,"of expr","is = " ,salary3)
elif(int(exp3)>=2 and int(exp3)<5):
    salary3=int(salary3)+(int(salary3)*.2)
    print("salary for",emp3,"for",exp3,"of expr", "is = ",salary3)

































