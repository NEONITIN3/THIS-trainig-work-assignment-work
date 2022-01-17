#function
#function name put in lower case its show meture coder
#def is the keyword which is difine that its is functioon
#def funname():

def fun(): #no parameterisez function
         print("neo nitin function work")
fun() #its called calling of function

print(type(fun))
#function

'''you want to print that line 10 times so'''
for i in range(5):
    fun()

def add(a,b,m): #parameterised funstion
    print(a+b+m)
add(2,3,4)

#but if u dont know that how many values going to pass then used *args

def sum_fun(*args): #parameterised funstion
    print(args)
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
sum_fun(1,2,3,4,5,6,7,8,9,10)
sum_fun(1,2,3,4,5,6,7,8)
sum_fun(1,2,3,4,5)
sum_fun(6,7,8,9,10)



def fun2(*args,**kwargs):
    print(args)
    print(kwargs)
num=(10,20,30,30)
d1={'name':'Ram',"course":"B.tech","email":"ram@gmail.com"}
fun2(*num,**d1)